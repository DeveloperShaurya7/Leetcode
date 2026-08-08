class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        next_pos = [-1] * m

        p = n - 1

        for j in range(m - 1, -1, -1):
            while p >= 0 and word1[p] != word2[j]:
                p -= 1

            if p < 0:
                break

            next_pos[j] = p
            p -= 1

        ans = []
        p = 0
        used = False

        for j in range(m):
            while p < n:

                if word1[p] == word2[j]:
                    ans.append(p)
                    p += 1
                    break
                
                if not used:
                    if j == m - 1:
                        ans.append(p)
                        p += 1
                        used = True
                        break

                    if next_pos[j + 1] > p:
                        ans.append(p)
                        p += 1
                        used = True
                        break

                p += 1

            else:
                return []

        return ans
     
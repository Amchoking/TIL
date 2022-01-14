class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lens=len(s)
        answer=['a' for i in range(lens)]
        for i in range(lens):
            index=indices[i]
            answer[index]=s[i]
        return ''.join(answer)

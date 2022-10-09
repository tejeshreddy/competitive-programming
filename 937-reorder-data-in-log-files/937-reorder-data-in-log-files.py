class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        solution_ll = []
        solution_dl = []
        
        for i in logs:
            if i[-1].isalpha():
                solution_ll.append(i)
            else:
                solution_dl.append(i)

        solution_ll = sorted(solution_ll, key = lambda x: (x.split(" ")[1:], x.split(" ")[0]))
        return solution_ll + solution_dl
        
            
        print(solution)

        
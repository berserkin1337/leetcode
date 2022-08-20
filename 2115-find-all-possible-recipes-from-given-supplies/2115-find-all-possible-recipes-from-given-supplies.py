class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        
        for recipe,ingredient in  zip(recipes,ingredients):
            for i in ingredient:
                graph[i].append(recipe)
                inDegree[recipe] += 1
        queue = supplies[::]
        res = []
        
        while queue :
            ing = queue.pop(0)
            
            if ing in recipes :
                res.append(ing)
            for node in graph[ing]:
                inDegree[node] -=1
                if inDegree[node] == 0 :
                    queue.append(node)
                    
        return res
        
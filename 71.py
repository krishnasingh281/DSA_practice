class Solution:
 def simplifyPath(self,path: str) -> str:
    parts = path.split("/")
    folders = []

    for part in parts:
        if part == "" or part == ".":
            continue
        elif part == "..":
            if len(folders) > 0:
                folders = folders[:-1]  
        else:
            folders = folders + [part]  

    return "/" + "/".join(folders)
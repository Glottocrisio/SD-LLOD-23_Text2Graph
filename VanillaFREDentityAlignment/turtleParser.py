import unicodedata
import os
import removePOS
import removeDisconnectedThings
import mergeSimilarity




def turtleParser(file="turtleBerlusconi.ttl"):
   #turtlefile = open(file, "rt", encoding="utf-8")
   #turtlefile = typefile.read()
   #output file to write the result to
   #turtlefileparsed = open("turtlefileparsed"+str(file)+".txt", "wt",  encoding="utf-8")
   mergeSimilarity.mergeSimilarity(file)
   #removePOS(turtlefile)
   #removeDisconnectedThings(turtlefile)
   #add here all other possible functions
   #parsedFinalString= ""
   #with open(turtlefileparsed, "w",  encoding="utf-8") as f:  
   #     f.write(parsedString)
   #turtlefile.close()
   #turtlefileparsed.close()
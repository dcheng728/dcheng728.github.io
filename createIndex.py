import os
import markdown


   
f = open("index.html", "w")

f.write("""<!DOCTYPE html>
<html lang="en">


<head>
<title>solutions</title>

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\_\_(','\_\_)']]}});
</script>
<script type="text/javascript"
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>
<h1>Solutions</h1>\n""")

def summaryBlock(margin, content):
    f.write("""<summary style="margin-left:""")
    f.write(str(margin)) 
    f.write("""px;">\n""")
    f.write(content)
    f.write('<span class="icon"></span></summary>\n')
    
def pBlock(margin, content):
    f.write("""<p style="margin-left:""")
    f.write(str(margin)) 
    f.write("""px;">\n""")
    f.write(content)
    f.write('<span class="icon"></span></p>\n')
    
def divBlock(margin, content):
    f.write("""<div style="margin-left:""")
    f.write(str(margin)) 
    f.write("""px;border: 3px dashed black; background-color:powderblue;"">\n""")
    f.write(content)
    f.write('<span class="icon"></span></div>\n')
    
def link(margin,url,text):
    f.write("""<div style="margin-left:""")
    f.write(str(margin)) 
    f.write("""px;">\n""")
    f.write('''<a href="''')
    f.write(url)
    f.write('''">''')
    f.write(text)
    f.write("""</a></div>\n""")
    
def removeJunk(toRemove):
    removeList = ['.gitignore', '.DS_Store', 'createIndex.py', 'index.html', '.git', '.obsidian']
    for removeItem in removeList:  
        try: 
            toRemove.remove(removeItem)
        except:
            pass
    return toRemove

def readMarkdown(SOURCE):
    with open(SOURCE, 'r') as f:
        tempMd= f.read()

    return markdown.markdown(tempMd)

def dig(file_or_dir,level):
    to_display = file_or_dir.split('/')[-1]
    
    
    
    if os.path.isdir(file_or_dir):
        f.write('<details>\n')
        summaryBlock(level * 30, to_display)
        
        new_files = removeJunk(os.listdir(file_or_dir))
        new_files.sort()
        
        
        for new_file in new_files:
            dig(file_or_dir + '/' + new_file,level + 1)
            
        f.write("</details>\n")
            
    else:
        
        if file_or_dir.split('.')[-1] == 'md':
            f.write('<details>\n')
            summaryBlock(level * 30, to_display)
            divBlock((level+1)*30,readMarkdown(file_or_dir))
            f.write("</details>\n")
            
        if file_or_dir.split('.')[-1] == 'pdf':
            link(level * 30,file_or_dir,to_display)
            
    
            
    
print(removeJunk(os.listdir(os.getcwd())))
        

for filename in removeJunk(os.listdir(os.getcwd())):
    dig(filename,0)

    
    

# for book in books:
#     f.write('<details>\n')
#     f.write('<summary>\n')
#     f.write(book)
#     f.write('<span class="icon"></span></summary>')
    
#     folderOrPDFs = os.listdir(os.getcwd() + '/' + book)
#     removeDSStore(folderOrPDFs)
#     folderOrPDFs.sort()
    
#     for folderOrPDF in folderOrPDFs:
#         if os.path.isdir(os.getcwd() + '/' + book + '/' + folderOrPDF):
            
#             PDFs = os.listdir(os.getcwd() + '/' + book + '/' + folderOrPDF)
#             removeDSStore(PDFs)
#             PDFs.sort()
            
#             f.write('<details>\n')
#             summaryBlock(20, folderOrPDF)
            
#             for PDF in PDFs:
#                 f.write('<details>\n')
#                 solutionInfo = (PDF.split('.')[0]).split('_')
#                 solutionToDisplay = solutionInfo[-1]
                
#                 summaryBlock(40, solutionToDisplay)
                
#                 link(100,book+'/'+folderOrPDF+'/'+PDF,solutionToDisplay)
                
#                 f.write("</details>\n")
#             f.write("</details>\n")
            
#         else:
#             solutionInfo = (folderOrPDF.split('.')[0]).split('_')
#             solutionToDisplay = solutionInfo[-1]
#             f.write('<details>\n')

#             summaryBlock(40,solutionToDisplay)
            
#             link(100,book+'/'+folderOrPDF,folderOrPDF)

#             f.write("</details>\n")

#     f.write("</details>\n")
        
            
f.write("""</body>\n""")
f.write("""</html>""")
f.close()

import os
import markdown

biblography = {'(ced)griffiths':  'Griffiths. <i>Intro. to Electrodynamics</i>, 4th ed.', 
               '(ced)jackson':    'Jackson. <i>Classical Electrodynamics</i>, 3rd ed. ',
               '(cm)goldstein':   'Goldstein, Poole & Safko. <i>Classical Mechanics</i>, 3rd ed.',
               '(gr)schutz':      'Schutz. <i>A first course in general relativity</i>.',
               '(particles)griffiths': 'Griffiths. <i>Intro. to Elementary Particles</i>, 1st ed.',
               '(sstate)kittel': 'Kittel. <i>Intro. to Solid State Physics</i>, 8th ed.',
               '(therst)callen': 'Callen. <i>Thermodynamics and an Intro. to Thermostatistics</i>, 2nd ed.',
               '(therst)fermi': 'Fermi. <i>Thermodynamics</i>.',
               '(therst)glazer wark': 'Glazer & Wark. <i>Stat. Mechanics A Survival Guide</i>.',
               '(therst)kittel': 'Kittel & Kroemer. <i>Thermal Physics</i>, 2nd ed. ',
               '(therst)pathria': 'Pathria & Beale. <i>Stat. Mechanics</i>, 4th ed.',
               '(qft)weinberg': 'Weinberg. <i>The Quantum Theory of Fields</i>, vol. 1,2.'}

subject_abbr_to_display = ['cm','ced','therst','particles','sstate', 'gr','qft']

subject_full_name = {'cm': 'Classical Mechanics',
                     'ced': 'Classical Electrodynamics',
                     'therst': 'Thermal and Statistical Physics',
                     'particles': 'Particle Physics',
                     'sstate': 'Solid State Physics',
                     'gr': 'General Relativity',
                     'qft': 'Quantum Field Theory'}

def summaryBlock(margin, content):
    holder = """<summary style="margin-left:{0}px;">\n{1}<span class="icon"></span></summary>\n""".format(margin, content)
    f.write(holder)

def hBlock(margin, content,num):
    holder = """<h{0} style="margin-left:{1}px;">\n{2}<span class="icon"></span></h{0}>\n""".format(num,margin,content)
    f.write(holder)

def pBlock(margin, content):
    holder = """<p style="margin-left:{0}px;">\n{1}<span class="icon"></span></p>\n""".format(margin,content)
    f.write(holder)
    
def divBlock(margin, color, content):
    holder = """<div style="margin-left:{0}px;border: 3px dashed black; background-color:{1};">\n{2}<span class="icon"></span></div>\n""".format(margin,color,content)
    f.write(holder)
    
def link(margin,url,text):
    url = url.replace("?", "%3F")
    holder = """<div style="margin-left:{0}px;">\n<a href="{1}" target="_blank">{2}</a></div>\n""".format(margin,url,text)
    f.write(holder)
    
def removeJunk(toRemove):
    removeList = ['.gitignore', '.DS_Store', 'createIndex.py', 'index.html', '.git', '.obsidian']
    for removeItem in removeList:  
        try: 
            toRemove.remove(removeItem)
        except:
            pass
    return toRemove

def orderChapters(fileList):
    indices = []
    for fileName in fileList:
        try: 
            index = int(fileName.split('-')[0])
        except:
            index = 10000
        indices.append(index)
        
    sortedFiles = [x for _, x in sorted(zip(indices, fileList))]

    return sortedFiles

def orderDocuments(fileList):
    indices = []
    for fileName in fileList:
        if len(fileName.split('.')) < 2: #directory, sorted to last
            indices.append(1e50)
        else:
            try: 
                index = (fileName.split('.')[0]).split('_')[2] #getting the label of the exercise
                if index.isdigit():
                    indices.append(int(index))
                
                elif index[0].isdigit():
                    new_index = ''.join(c for c in index if c.isdigit())
                    indices.append(int(new_index))

                else:
                    indices.append(1e15)

            except:
                indices.append(1e30)

    sortedFiles = [x for _, x in sorted(zip(indices, fileList))]

    return sortedFiles


def orderFiles(fileList,lvl):
    if  lvl == 1: #level 1 is book title, so the files obtained are chapters in books
        return orderChapters(fileList)
    
    if  lvl == 2: #level 2 is chapters in books, so the files contained are documents (.pdf, .md, etc)
        return orderDocuments(fileList)

    else:
        return fileList

def readMarkdown(SOURCE):
    with open(SOURCE, 'r') as f:
        tempMd= f.read()

    return markdown.markdown(tempMd)



def dig(file_or_dir,level):
    to_display = file_or_dir.split('/')[-1]

    if level == 1: #level 1 is book title
        to_display = biblography[to_display]

    if os.path.isdir(file_or_dir):
        f.write('<details>\n')
        summaryBlock(level * 30, to_display)


        new_files = orderFiles(removeJunk(os.listdir(file_or_dir)),level)
        
        for new_file in new_files:
            dig(file_or_dir + '/' + new_file,level + 1)
            
        f.write("</details>\n")
            
    else:
        if file_or_dir.split('.')[-1] == 'md':
            f.write('<details>\n')
            summaryBlock(level * 30, to_display)
            divBlock((level+1)*30,'LightGray',readMarkdown(file_or_dir))
            f.write("</details>\n")
            
        if file_or_dir.split('.')[-1] == 'pdf':
            if len(to_display.split('_')) == 3:
                to_display = 'exercise ' + to_display.split('_')[1]+ '.' + to_display.split('_')[2]
            link(level * 30,file_or_dir,to_display)



f = open("index.html", "w")

f.write("""<!DOCTYPE html>
<html lang="en">


<head>
<title>Davidson Cheng's Physics Study</title>

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
        
<h1>Davidson Cheng's Physics Study</h1>\n

<p>This website tracks my progress in self-studying physics. 
        The contents are mostly my notes and solutions to exercises in books. 
        The math in notes might not display properly depending on browser.</p>

<hr>

""")
    
subject_abbr_and_booktitle_list = removeJunk(os.listdir(os.getcwd()))



for subject_abbr in subject_abbr_to_display:
    hBlock(0,subject_full_name[subject_abbr],3)
    for filename in subject_abbr_and_booktitle_list:
        splitted = filename.split(')')

        if len(splitted) == 2:
            subject_abbr_curr = splitted[0][1:]
            book_abbr_curr = splitted[1]
            if subject_abbr_curr == subject_abbr:
                dig(filename,1)

f.write("<hr>")
            
f.write("""</body>\n""")
f.write("""</html>""")
f.close()

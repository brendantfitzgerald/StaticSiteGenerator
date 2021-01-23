import markdown
import os
from datetime import datetime
### Anatomy of a Page
#! Header 
## Post Title - from Filename
## Date - from code
#! Body
## Post Content - From markdown in file
#! Footer - from code
## Link to Post List
## Link to Resume
## Link to Main Site (if there is one)

### Anatomy of this Script
# Check txt against HTML folders
# Create HTML files for any txt files that don't have one
## Following the "Anatomy of a Page" at the top of this file
# Update the "Post List" page with the new HTML file
# Upload the new/updated HTML files to AWS S3

def main():
    g_txtPath = "/home/brendan/Code/SitePosts/YesFitz/txt/"
    g_htmlPath = "/home/brendan/Code/SitePosts/YesFitz/HTML/"
    g_txtFiles = os.listdir(g_txtPath)
    g_htmlFiles = os.listdir(g_htmlPath)
    g_footer = open(g_txtPath+"Footer","r",encoding="utf-8").read()
    MDtoHTML(g_txtPath,g_txtFiles,g_htmlPath,g_htmlFiles,g_footer)
    CreateAllPosts(g_htmlFiles,g_htmlPath,g_footer)
    g_SiteName = "YesFitz"

def MDtoHTML(txtPath,txtFiles,htmlPath,htmlFiles,footer):
    for Post in txtFiles:
        if (Post == "Footer"):
            continue
        if Post+".html" in htmlFiles:
            print(Post+" has already been converted.")
        else:
            with open(txtPath+Post, "r", encoding="utf-8") as input_file:
                PostText = input_file.read()
                PostText = AppendHeader(PostText,Post)
                PostText = AppendFooter(PostText,footer)

            PostHtml = markdown.markdown(PostText)
            with open(htmlPath+Post+".html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
                output_file.write(PostHtml)

def AppendFooter(text,footer):
    text = text+footer
    return text

def AppendHeader(text,title):
    date = datetime.now().strftime('%Y%m%d')
    header = "#"+title+"\n"+"#####"+date+"\n"
    text = header+text
    return text

def CreateAllPosts(htmlFiles,htmlPath,footer):
    PostList = "#YesFitz Posts"
    for Post in htmlFiles:
        PostTitle = Post[0:len(Post)-5]
        NewPost = "\n\n"+"["+PostTitle+"](./"+Post+")"
        if (PostTitle == "allposts"):
            continue
        else:
            PostList = PostList+NewPost
    PostList = AppendFooter(PostList,footer)
    PostList = markdown.markdown(PostList)
    with open(htmlPath+"allposts.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
                output_file.write(PostList)




main()
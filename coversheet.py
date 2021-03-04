import fitz # pdf stuff
import sys

# add a cover sheet in the form of name id and title to the desired pdf
def AddCoverSheet(name, idNum, title, pdf_path):
    cover_pdf = fitz.open() # new pdf handle
    cover_page = cover_pdf.newPage() # first and only page.. width=595, height=842
    
    pdf = fitz.open(pdf_path) # handle to pdf needing cover
    
    # add title, name, id to the coversheet
    rectangles = [fitz.Rect(97.5, 200, 497.5, 300), fitz.Rect(197.5, 450, 397.5, 500), fitz.Rect(197.5, 500, 397.5, 550)] # [title, name, id]
    cover_page.insert_textbox(rectangles[0], title, fontsize=44, align=1)
    cover_page.insert_textbox(rectangles[1], name, fontsize=16, align=1)
    cover_page.insert_textbox(rectangles[2], idNum, fontsize=16, align=1)
    
    cover_pdf.insert_pdf(pdf,) # add behind cover
    pdf.close() # close original handle so we can overwrite pas save
    cover_pdf.save(pdf_path) # save the file
    


if __name__ == '__main__':
    AddCoverSheet(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))
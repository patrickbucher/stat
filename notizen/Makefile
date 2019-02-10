EPUBPARAMS=--toc -N -s -t epub
PDFPARAMS=--toc -N -s -t latex --pdf-engine=xelatex -V documentclass=scrartcl -V papersize=a4 -V lang=en -V urlcolor=blue -V linkcolor=blue -V fontsize=10pt -V geometry='top=1in,right=1in,left=1in,bottom=1.5in'
FONTS=-V mainfont='DejaVu Serif' -V sansfont='DejaVu Sans' -V monofont='DejaVu Sans Mono'
DATE=-V date="`date +'%Y-%m-%d'`"

all: notes.pdf notes.epub

notes.pdf: *.md
	pandoc $(PDFPARAMS) $(FONTS) $(DATE) *.md -o notes.pdf

notes.epub: *.md
	pandoc $(EPUBPARAMS) $(DATE) *.md -o notes.epub

clean:
	rm -f notes.pdf
	rm -f notes.epub

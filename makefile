FILES := 130010038.pdf 
PICS := $(wildcard *.png)
PYC := $(wildcard *.pyc)

main :   
	cd source && python 130010038.py
	jupyter nbconvert --to html source/130010038.ipynb
	mv source/130010038.html ./output
	make everything

everything: 
	cp source/bib_file.bib . 
	pdflatex -output-directory output source/130010038.tex 
	bibtex output/130010038.aux
	pdflatex -output-directory output source/130010038.tex
	pdflatex -output-directory output source/130010038.tex
	rm bib_file.bib

.PHONY: clean test
test:
	pytest source/130010038test.py
clean:	 
	rm -rf output

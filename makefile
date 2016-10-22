#cd ./output;\ 
FILES := paper.pdf
AUXFILES := $(FILES:.pdf=.aux)
LOGFILES := $(FILES:.pdf=.log)
BBLFILES := $(FILES:.pdf=.bbl)
BLGFILES := $(FILES:.pdf=.blg)
OTHERS := $(wildcard *.synctex.gz)
PICS := $(wildcard *.png)
PYC := $(wildcard *.pyc)

main :
	python LCRplots.py
	make pdf

pdf : $(FILES:.pdf=.tex)
	make paper.pdf

%.pdf: %.tex
	pdflatex $<
	bibtex `echo $< |cut -d "." -f1`.aux
	pdflatex $<
	pdflatex $<

.PHONY: clean clean-all
clean-all:
	$(RM) $(AUXFILES) $(FILES) $(LOGFILES) $(BBLFILES) $(BLGFILES) $(OTHERS) $(PICS) $(PYC)

clean:
	$(RM) $(AUXFILES) $(LOGFILES) $(BBLFILES) $(BLGFILES) $(OTHERS) $(PICS) $(PYC)
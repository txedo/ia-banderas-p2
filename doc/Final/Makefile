TEX_FILES=Documentacion.tex Bibliografia.bib


all: Documentacion.pdf


Documentacion.pdf: $(TEX_FILES)
	pdflatex $<
	bibtex Bibliografia
	pdflatex $<
	pdflatex $<	


alt-all:
	rubber -d Documentacion.tex


clean:
	$(RM) *~ *.out *.log *.aux *.toc *# *.dvi *.blg *.lof *.lot *.maf *.mtc*

default: clean
	sh make_index.sh > index.markdown

clean:
	-rm *.markdown

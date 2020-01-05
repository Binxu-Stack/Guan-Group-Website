# Guan-Group-Website
Website for Guan Group

A: What is the basic idea to develop this website?

Q: Borrowthe basic design philosophy from Django, and try to 
split the data, contant and view in a simple way, since it is 
only a very small website.

Q: How to update the basic views?

A: Modify `1-Resource/base.html`

Q: How to update the content in different pages?

A: For example, I want to update the content in index.html.
* Contant update: Update index content via modifying `1-Resource/index-content.html`.
* View update: run the script `1-Resource/create_view.py`, and the new views will be created in
the `2-view`.

Q: Develop environment?

A: python and bash.


Feature (TODO):
* Surpporing markdown to write new content.


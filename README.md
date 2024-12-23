# egeGenie

# to run

steps to run:
## install requirements
`pip install -r req_21_10_24.txt`
## run the module
`python3 -m src.pdfengine.loader.setup.genie`

- While runnig the above code, make sure you are in directory "egeGenie"
- You can chat with the bot once you run the `genie` module.



# Over all architecture

while we call `python3 -m src.pdfengine.setup.genie` the flow is as follows:
- genie-object is gets created with given *secret key, given model,  and pdf file path*. The *pdf file path* is used to parse pdf(to extract the data from pdf as text to embed them and store as vectors)
- after creating the genie object we call ***chat_with_genie*** method. That method loops over the ***take_input*** *method*, which takes input until you enter `e` in terminal as input.

## How does the ***retrieval-chain*** get create

- we only make retrieval-chain onece at `rc = self.prepare_chain()`
- when the controller calls the `prepare_chain()`, the `prepare_chain` method
creates `RetrivalChain` ***object***, creates retrieval chain.
---
- While creating RetrivalChain, we have to pass ***vector***, which we get from `VectorRetriever().retriever` method.
- We are importing VectorRetriever class from `src.pdfengine.setup.embedding`
---
- when we call `VectorRetriever().retriever`, we create `PDFMarkdownProcessor()` ***object***, and call *get_document* ***method*** by `loader.get_document()`
---
- from `process_pdf` ***module*** feel free to explore...
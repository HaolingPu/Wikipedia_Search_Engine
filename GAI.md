# GEN AI P5 Chatbot Feedback

### Example:     {: #Q01}
- [ ] Yum
- [x] Yuk

## Background

### How many ULCS courses has group member 1 taken including the current semester? {: #Q02}
1
### How many ULCS courses has group member 2 taken including the current semester? {: #Q03}
2
### How many ULCS courses has group member 3 taken including the current semester? {: #Q04}
4

## General
### Approximately how many interactions did you have with the bot on project 5? {: #Q05}
- [ ] 0-3
- [x] 4-10
- [ ] 11-50
- [ ] 51+

### Mark all the topics where the bot was helpful: {: #Q06}
- [x] Spec questions
- [ ] Design
- [ ] Debugging
- [x] Conceptual questions
- [ ] Explaining test cases
- [ ] Setup / toolchain
- [ ] Implementation / code suggestions

### Would a similar bot be helpful for other projects? {: #Q07}
- [x] Yes
- [ ] No
- [ ] Unsure

### Our group used the bot instead of posting on Piazza {: #Q08}
- [ ] Never
- [ ] Rarely
- [x] Sometimes
- [ ] Often
- [ ] Always

### Our group used the bot instead of going to Office Hours {: #Q09}
- [ ] Never
- [ ] Rarely
- [x] Sometimes
- [ ] Often
- [ ] Always

### Using the bot instead of Piazza or Office Hours saved time {: #Q10}
- [ ] Yes
- [x] No
- [ ] Unsure

### The bot gave more helpful answers than ChatGPT {: #Q11}
#### (Reminder: Course policy permits the use of generative AI for projects (https://eecs485.org/syllabus.html#generative-ai-copilot-chatgpt))
- [ ] Never
- [ ] Rarely
- [x] Sometimes
- [ ] Often
- [ ] Always
- [ ] I did not use ChatGPT

### Given the choice, which bot would you prefer to use for project help? {: #Q12}
- [ ] EECS485 bot (Reducey)
- [ ] ChatGPT
- [x] Both
- [ ] Neither

### Please explain your answer to the previous question. {: #Q13}
ChatGPT is still more powerful than the Bot we think.

#### (Optional) Overall, do you have any feedback on the bot? {: #Q14}
It is slow. And sometimes not answer the question accurately.

## Interaction 1
### Prompt {: #Q15}
I am write the P5 in the index server part, and I found that the output of hits is disordered. How to solve this problem?

### Response {: #Q16}
If you're noticing that the output of hits is disordered in the index server part of the project, there's a high chance that the issue lies in the way you're processing the search results before sending them to the client. To ensure an ordered output, follow these steps:



Sort the Results: Upon fetching the hits from the inverted index, sort them according to the criteria specified by the project (often by relevance, document ID, or a combination). Depending on the implementation, this sorting could either happen during the query processing stage or right before sending the results back to the client.



Check Query Parsing: Ensure the search query is being parsed correctly and is retrieving results in a predictable manner. Issues here could lead to erratic results ordering.



Examine Merge Algorithm: Since the index may be made up of sub-indexes that are merged, make certain the merge algorithm properly preserves the order of the hits.



Review Data Structures: The choice of data structure for storing and retrieving hits can affect order. Review your choice and ensure it's suitable for maintaining a sorted order.




### Was this response helpful? {: #Q17}
- [ ] Yes
- [x] No

### To the best of your knowledge, did it answer your question correctly: {: #Q18}
- [ ] Yes
- [ ] No
- [x] Unsure

### (Optional) Anything else you want to tell us about this interaction? {: #Q19}
This should actually give a brief answer: "You should order the hits based on the score of each doc."

## Interaction 2
### Prompt {: #Q20}
what is the relationship between df and idf?

### Response {: #Q21}
The relationship between document frequency (df) and inverse document frequency (idf) is a reciprocal one. In the context of information retrieval, df for a term is the number of documents in the collection that contain that term. The more often a term appears in documents across the collection, the higher its document frequency.


Inverse document frequency, on the other hand, is a measure intended to reflect how important a term is in the entire collection of documents, which is calculated based on the total number of documents (N) divided by the document frequency (df) for the term, and then taking the logarithm of that quotient:


idf(tk) = log(N/df(tk))


So, as the document frequency (df) for a term increases (meaning the term is common across many documents), the inverse document frequency (idf) decreases, as it's assumed that common terms are less informative. Conversely, for rare terms that appear in fewer documents, the document frequency (df) is lower, resulting in a higher inverse document frequency (idf), suggesting the term is of greater relative importance within the collection of documents.


In summary, the idf for a term becomes greater as the number of documents it appears in (df) becomes fewer, indicating the term's uniqueness and potential significance in the collection of documents.



### Was this response helpful? {: #Q22}
- [x] Yes
- [ ] No

### To the best of your knowledge, did it answer your question correctly: {: #Q23}
- [x] Yes
- [ ] No
- [ ] Unsure

### (Optional) Anything else you want to tell us about this interaction? {: #Q24}
FIXME

## Interaction 3
### Prompt {: #Q25}
I don't know how to implement init.py and model.py. It is not specified in the spec.

### Response {: #Q26}
Hello student,


I understand that you're finding it difficult with understanding what should go into your __init__.py and model.py files, and that the specifications do not offer clear guidance on this.


The purpose of the __init__.py file is to indicate to Python that the directory should be treated as a package. This file can be empty, or it can contain valid Python code. For your case, based on the snippet you put:


from index.api import load_index  # noqa: E402 pylint: disable=wrong-import-position

It seems like you are using this file to import a specific function from a module to make it accessible to other parts of your application.


For your model.py, this file typically contains the classes that define the structure of your data. This is where you would define any database tables as Python classes if you're using an ORM (Object-Relational Mapping) like SQLAlchemy or the Django ORM.


Since you need to create an "inverted index" for each part respectively, named as "inverted_index_[num]," your model.py might contain definitions for these indices. While I cannot give you the exact code, I can provide an outline for what the file might contain:


class InvertedIndex0(db.Model):
    # define the structure for inverted_index_0 here
    
# ... similarly define other InvertedIndex classes for each part

Each InvertedIndex could have attributes like word, document, frequency, etc., based on what keys and values your inverted index is supposed to store. You would define methods to interact with the data just like you would in an ordinary Python class, except that these would correspond to database operations such as queries.


As for the init.py in the views, it typically is used to import the view functions. These may look like:


from .your_view_file import some_api_view_function

I encourage you to look at the examples from Project 2/3, which your instructor mentioned, and adapt similar patterns that were used there within your current project.


Remember, even though you're drawing inspiration from your past projects, you'll need to make sure that any code you're reusing is adapted to fit the specifications and requirements of this current project.


And of course, if you continue to feel stuck, feel free to provide any error messages or more detail about the current specifications so we can figure it out together. Good luck!


### Was this response helpful? {: #Q27}
- [x] Yes
- [ ] No

### To the best of your knowledge, did it answer your question correctly: {: #Q28}
- [x] Yes
- [ ] No
- [ ] Unsure

### (Optional) Anything else you want to tell us about this interaction? {: #Q29}
FIXME
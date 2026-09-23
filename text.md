Generative ai :
prompt -> LLM -> output

GEN AI - is a type of AI that can create new content such as text, images, audio, video or code by learning patterns from existing data.

Fraud detection 
AI model -> fraud or not modal (in smaller sense)

1. ML - we have statistical model and deep learning

In statistical ml -> we have XgBoost & Random forest
In deep learning -> we have Neural networks, CNN, RNN, Trandformers

* we also have rule -based systems, and on the other hand we have ml models.

* ATTENTION IS ALL YOU NEED. GOOGLE PUBLISHED THIS PAPER AND CAME OUT AS BREAKTHROUGH IN THE HISTORY OF AI.

* llM is finding the next token/ next word.
* there is a concept while doing prediction using LLM, we use a parameter temperature to make our model more creation (more predictable).

top-k-sampling parameter :
- defines the top 3 words while pred of new word.
- k=3 , we will top 3 words for prediction.

top-p-sampling :
- defines it as cumulative property.
- lets say we have p=0.9
- we will take first list of words who summation of cumulative property ois more than p-value

context window :
- means total no of tokens/ letters we can send to LLM in one second.

eg- gmail also used llm to predict next words.

OPEN AI - used a concept RLHF (Reinforcement learning with human feedback)

### langchain 
- is an ecosystem, it has 
1. langsmith 
-> for observability, evaluation, deployment and fleet (agent for the whole company)

2. langgraph 
-> to build reliable agents with low-level control
-> eg : dslr camera with automatic control (no manual control)

3. langchain

### uv
- uv init -> create a py project and all other required files
- uv sync -> sync the project.toml dependencies and install all packages
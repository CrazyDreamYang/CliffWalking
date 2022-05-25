# CliffWalking-with-different-methods
## About It

<div align=center>
<img src="https://github.com/kingofYC/CliffWalking/blob/main/result/cliffwalking.png" > 
</div>

* CliffWalking is a classic environment of **OpenAI gym**. This project create a new render function to dispaly interaction between the environment and the agent。
* Additionally, I use two graph search methods to find the optimal path between the start and end points. The two methods are **A*** and **Dijkstra**.

## Get Started

```bash
git clone https://github.com/kingofYC/CliffWalking.git
cd CliffWalking
pip install requirements.txt
```

* **Dijkstra**

```bash
python dijkstra_search.py
```
<div align=center>
<img src="https://github.com/kingofYC/CliffWalking/blob/main/result/dijkstra.png"  width="30%" height="30%" > 
</div>

* **A***

```bash
python a_star_search.py
```
<div align=center>
<img src="https://github.com/kingofYC/CliffWalking/blob/main/result/a_star.png"  width="30%" height="30%" > 
</div>

* RL- Q_Learning

```bash
python q_learning.py
```
<div align=center>
<img src="https://github.com/kingofYC/CliffWalking/blob/main/result/q_learning.gif"  width="30%" height="30%" > 
</div>

>q_table
<div align=center>
<img src="https://github.com/kingofYC/CliffWalking/blob/main/result/q_table_q_learing.png"  width="60%" height="60%" > 
</div>

```bash
python sarsa.py
```
<div align=center>
<img src="https://github.com/kingofYC/CliffWalking/blob/main/result/sarsa.gif"  width="60%" height="60%" > 
</div>

>q_table
<div align=center>
<img src="https://github.com/kingofYC/CliffWalking/blob/main/result/q_table_sarsa.png"  width="60%" height="60%" > 
</div>
  

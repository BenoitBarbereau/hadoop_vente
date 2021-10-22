# hadoop_vente


## INSTALL

```
git clone https://github.com/BenoitBarbereau/hadoop_vente.git
```

## USAGE

```
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar -input ./sales_world_10k.csv -output ./test -mapper "python3 /home/mbds/mapper_analyse_finance.py X" -reducer "python3 /home/mbds/reducer_analyse_finance.py X"
```
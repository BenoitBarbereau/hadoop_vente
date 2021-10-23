# hadoop_vente


## INSTALL

```
git clone https://github.com/BenoitBarbereau/hadoop_vente.git
```

## USAGE

```
hadoop fs -put ./ventes/sales_world_10k.csv
```

```
chmod 777 reducer_analyse_finance.py
```


```
chmod 777 mapper_analyse_finance.py
```


● Obtenir le profit total obtenu par région du monde.

```
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar -input ./sales_world_10k.csv -output ./test2 -mapper "python3 /home/mbds/ventes/mapper_analyse_finance.py Region" -reducer "python3 /home/mbds/ventes/reducer_analyse_finance.py Region"
```

● Obtenir le profit total obtenu par pays.

```
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar -input ./sales_world_10k.csv -output ./test -mapper "python3 /home/mbds/mapper_analyse_finance.py country" -reducer "python3 /home/mbds/reducer_analyse_finance.py country"
```

● Obtenir le profit total obtenu par type d’item.
> La quantité de ventes en ligne.
> La quantité de ventes hors ligne


```
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar -input ./sales_world_10k.csv -output ./test -mapper "python3 /home/mbds/mapper_analyse_finance.py Item" -reducer "python3 /home/mbds/reducer_analyse_finance.py Item"
```



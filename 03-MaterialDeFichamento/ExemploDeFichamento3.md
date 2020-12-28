# On the impact of energy-saving strategies in opportunistic grids

Ponciano, Lesandro and Brasileiro, Francisco (2010) "On the impact of energy-saving strategies in opportunistic grids," 11th IEEE/ACM International Conference on Grid Computing, Brussels, pp. 282-289, doi: [10.1109/GRID.2010.5698003](https://doi.org/10.1109/GRID.2010.5698003).

## 1. Fichamento de Conteúdo

O artigo trata da economia de energia na execução de aplicações _Bag-Of-Tasks_ (BoT) em infraestrutura de computação distribuída que usa o poder computacional de computadores que não estão em uso pelos seus usuários. Esse é o caso das grades computacionais oportunistas. Quando são submetidas, aplicações BoT usam muitos computadores da infraestrutura, cada um para executar uma tarefa da aplicação. Quando não há uma aplicação a ser executada, tais computadores ficam ociosos esperando a chegada de uma nova aplicação. Nesses momentos eles consomem energia em fazer qualquer computação útil. Diante desse problema, o artigo investiga o uso de três grupos de estratégias de economia de energia: 1) _sleeping states_, que são standby e hibernate; 2) _wake-up strategies_, que são Most Recently Sleeping (MRS) e Energy Aware (EA); e, 3) _scheduling strategies_, que são First Come First Served (FCFS), Fastest Processor to Largest Task (FPLT), Most Energy-Efficiency First (MEEF), Most Energy-Efficient to Largest Task (MEELT). São refeitas simulações da grade com até 350 máquinas e medindo economia de energia e o _slowdown_ em comparação ao _baseline_, que é manter as máquinas ociosas. Os resultados mostram que: 1) as estratégias são equivalentes quanto ao reduzido impacto no tempo de resposta, e 2) todas as _wake-up strategies_ geram economia de energia, sendo a EA gera maior economia que o MRS em cenário de alta contenção; 3) o _sleeping state_ hibernate também gera maior economia que o estado standby, sendo que ambos geram economia em relação ao estado ocioso.

## 2. Fichamento Bibliográfico
* _Bag-of-Tasks_ (BoT, aplicação do tipo saco-de-tarefas): aplicação composta por uma grande quantidade de tarefas que não se comunicam entre si e que podem ser executadas de forma independente uma das outras (página 1)
* _Wake-up strategy_ (estratégia de escolha do recurso a ser acordado): usada para escolher qual máquina acordar primeiro quando chegar uma nova aplicação para ser executada (página 5)
* _Sleeping states_ (estratégia de dormência): definidas pela Advanced Configuration and Power Interface (ACPI) e em que partes da máquina são desligadas, gerando economia de energia em relação a manter a máquina ociosa (página 5) 
* _Scheduling strategy_ (estratégia de escalonamento): usada para escolher qual máquina deve executar cada tarefa. (página 5)


## 3. Fichamento de Citações
* _"Opportunistic grids are distributed computing infrastructures that harvest the idle computing cycles of computing resources geographically distributed."_ (página 1)
* _"We measured the energy savings of the strategies in a scenario A by comparing the energy consumption of this scenario with the energy consumption of a similar scenario where the only difference is that machines are never placed in a sleeping state, i.e. they can only be in the owner, running and idle states"_  (página 4)
* _"The makespan of a BoT job is defined as the difference between the earliest time of submission of any of its tasks, and the latest time of completion of any of its tasks."_ (página 4)
* _"We assumed that all jobs submitted to the grid are CPU-bound, which facilitated the calculation of the energy consumption; other studies have also made a similar simplification"_ (página 5)
* _"To represent the variation in the availability of the machines over time, we used a trace of a desktop grid that displays data on the use of machines, identifying the periods when the machines are idle"_ (página 5)
* _"The availability of real workloads of BoT applications is rather limited. Thus, we decided to also use synthetic workloads to complement our investigation. To generate the different workloads considered, we used the workload model proposed by Iosup et al. [11]."_ (página 6)
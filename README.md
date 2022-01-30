# Welcome to IonQ + Microsoft Joint Challenge @ MIT iQuHACK 2022!

<p align="left">
  <a href="https://azure.microsoft.com/en-us/solutions/quantum-computing/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488491-609828a4-cd1f-4076-b5b2-a8d9fc2d0fa4.png" width="30%"/> </a>
  <a href="https://ionq.com/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488159-da95eb05-9277-4abe-b1ba-b49871d563ed.svg" width="20%" style="padding: 1%;padding-left: 5%"/></a>
  <a href="https://iquhack.mit.edu/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151647370-d161d5b5-119c-4db9-898e-cfb1745a8310.png" width="8%" style="padding-left: 5%"/> </a>
  
</p>


Quantum computing has many exciting applications in chemistry, machine learning, and optimization – but we've only scratched the surface of the possibilities as a civilization, just like classical computing in the 1950s. We hope you all go on to do quantum algorithms research that will revolutionize every aspect of society for the better!

Today, though, we've got just 26 hours, and we'd like you to use a quantum computer to build a game, or a component of a game.

The possibilities should feel as big as the ones offered by your regular computer! A few ideas to juice your thinking:
* Use a quantum computer as a random number generator or noise source for
  - seeding behaviors
  - procedurally generating maps or music
* Use quantum logic itself as a gaming mechanism, whether for fun or education
* Apply Quantum Machine Learning to gameplay
* [Run Doom... on the universe?](https://www.smbc-comics.com/comic/qc)

You’ll be able to test your projects on a real ion trap quantum computer provided by IonQ (which [shoots lasers at individual atoms to compute](https://ionq.com/technology)).
*Remember that current devices are still NISQ, and noise can overtake the computation really fast. We recommend you experiment with circuits that use under a few dozen two-qubit gates.*

You can develop your project using any language supported by Azure Quantum: Q#, Qiskit, or Cirq.

## Using Azure Quantum
You should have received an invite to join quantum workspace https://portal.azure.com/52f51314-00bb-49b7-a28d-0b0a4be6d1c9. Join it, and use that workspace’s information to connect to Azure from the environment you’re using to work with the QDK:
* Subscription ID: b1d7f7f8-743f-458e-b3a0-3e09734d716d
* Resource group: aq-hackathons
* Workspace name: aq-hackathon-01
* Location: eastus

You can use it from Python by using the `azure-quantum` package as follows:

```python
from azure.quantum import Workspace
workspace = Workspace (
    subscription_id = "b1d7f7f8-743f-458e-b3a0-3e09734d716d",
    resource_group = "aq-hackathons",
    name = "aq-hackathon-01",
    location = "eastus"
)
```

Don't wait until the last moment to submit your programs! IonQ systems operate on a queue system. If you submit a program, it may take a few hours to complete. If you want to make sure you get your results back by Sunday morning, make sure to submit them by the end of day on Saturday.

## Submitting your projects
To submit your solutions:
1. Fork this repository to your GitHub account.
2. Commit your project to your forked repository.  
Include any files you consider relevant: the project itself, README including the description of the project and instructions on running the project, screenshots of results, any visualizations you've done, your project presentation, etc.
3. To submit your project, submit the link to your repository as detailed on https://iquhack.mit.edu/.
Your repository has to be made public at the time of the Hackathon end for us to be able to judge your solutions. We don't recommend making your work public early during the Hackathon, so as not to tempt other teams to borrow from your work. Let everybody enjoy their exploration!
*Note that GitHub doesn't allow to change visibility of the forks. You can either fork the repository, keep it public, and push your changes at the last possible moment, or you can duplicate the repository, make it private to work on it during the Hackathon, and make it public at the end of the Hackathon.*
4. If you want to write a blog post about your project, publish it shortly after the Hackathon ends and add a link to it to your GitHub repository.

## Judging

We'll be evaluating the projects based on several criteria, as detailed in this **rubric:** 

https://docs.google.com/document/u/1/d/e/2PACX-1vR5PVoInN_Fi42lIOchhblgGBPblgNyouj1XHukonZ4sdqY-p5ulS9TxdzvddEcDNFc5k_6teFyKzXv/pub

## Eligibility and prizes
The (1) highest team score will receive a **$500 Visa Gift Card** (physical or virtual) for the team. The next (4) highest team scores will receive a **$250 Visa Gift Card** (physical or virtual) for the team. The (5) winning teams will have an opportunity to present their projects to the Microsoft Quantum Team at a later date and time (to be scheduled after the results announcement).

Government officials and Microsoft employees are not eligible to participate in this challenge.

For the general rules on eligibility and hackathon participation, please refer to the [official rules](http://iquhack.mit.edu/).

## Resources

### Microsoft Quantum Development Kit installation

For this Hackathon, you have several options of setting up the QDK:

* local setup: you'll need the [standalone QDK](https://docs.microsoft.com/en-us/azure/quantum/install-command-line-qdk), and possibly (depending on what kind of project you decide to do) integration with [Q# Jupyter Notebooks](https://docs.microsoft.com/en-us/azure/quantum/install-jupyter-qkd) and/or with [Python](https://docs.microsoft.com/en-us/azure/quantum/install-python-qdk).
* qBraid: you can use qBraid virtual environment to develop your project. Here are the tutorials on how to [use Q# with qBraid](https://www.youtube.com/watch?v=E5JH1YfqSos) and [submit Azure Quantum jobs with qBraid](https://www.youtube.com/watch?v=WLAAqsqlYb8).
* Azure Portal: you can use the hosted notebooks experience to run code directly from Azure Portal.

### Documentation and tutorials

* [Azure Quantum and QDK documentation](https://docs.microsoft.com/quantum).
* [The Quantum Katas](https://github.com/Microsoft/QuantumKatas/) - a collection of tutorials and practice problems.
* Microsoft Learn learing path ["Quantum computing foundations"](https://docs.microsoft.com/learn/paths/quantum-computing-fundamentals/).
* [Q# developer blog](https://devblogs.microsoft.com/qsharp/).
* Azure Fridays episode [Quantum programming with Q# and running on hardware with Azure Quantum](https://www.youtube.com/watch?v=c9Df90CVHkc) shows the end-to-end quantum software development process with the QDK tools.

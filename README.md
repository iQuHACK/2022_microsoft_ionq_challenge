# Welcome to IonQ + Microsoft Joint Challenge at iQuHACK 2022!
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
* Workspace ID: aq-hackathon-01
* Storage account: aqhackathon01
* Location: eastus

Don't wait until the last moment to submit your programs! IonQ systems operate on a queue system. If you submit a program, it may take a few hours to complete. If you want to make sure you get your results back by Sunday morning, make sure to submit them by the end of day on Saturday.

## Submitting your projects
To submit your solutions:
1. Fork this repository to your GitHub account.
2. Commit your project to your forked repository.  
Include any files you consider relevant: the project itself, README including the description of the project and instructions on running the project, screenshots of results, any visualizations you've done, your project presentation, etc.
3. To submit your project, submit the link to your repository.  
Your repository has to be made public at the time of the Hackathon end for us to be able to judge your solutions. We don't recommend making your work public early during the Hackathon, so as not to tempt other teams to borrow from your work. Let everybody enjoy their exploration!
*Note that GitHub doesn't allow to change visibility of the forks. You can either fork the repository, keep it public, and push your changes at the last possible moment, or you can duplicate the repository, make it private to work on it during the Hackathon, and make it public at the end of the Hackathon.*
4. If you want to write a blog post about your project, publish it shortly after the Hackathon ends and add a link to it to your GitHub repository.

## Judging
We'll be evaluating the projects based on several criteria:
* Utility of Concept (20%)  
How useful is the final result? Usefulness here is not limited to quantum computing applications, but could also include educational utility as well. Note: while a finished product should of course score higher, if incomplete, consider the utility of the intended outcome.
* Technical Merit (20%)  
How well does the approach of this project exploit technical knowledge of concepts in quantum mechanics and quantum computing?
* Creativity (20%)  
How surprising, inventive, or otherwise “outside of the box” is the project?
* Relevance (20%)  
How well did the team tackle the challenge statement?
* Communication (20%)  
How clearly were the core goals and approach of the project presented in the final write-up and presentation (e.g. slides, presentation slides, README, tutorial)?

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

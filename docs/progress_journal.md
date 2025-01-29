# Team 5 Progress Journal - Rough Draft

## Team Meeting Notes

### Meeting 1 - January 21st

- First focus for us will be to work towards the **project proposal**

  - We have 5 weeks of work until this is due
  - The first step towards this will be to deeply understand the supporting material provided

- **For next week**, each team member must:

  - Be completely familiar with the info on the [Jersey Number Recognition Page](https://eval.ai/web/challenges/challenge-page/1952/overview) (SoccerNet Challenge 2023)
  - Review the following papers:
    - [A General Framework for Jersey Number Recognition in Sports Video](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Koshkina_A_General_Framework_for_Jersey_Number_Recognition_in_Sports_Video_CVPRW_2024_paper.pdf)
    - [Jersey Number Recognition using Keyframe Identification from Low-Resolution Broadcast Videos](https://arxiv.org/pdf/2309.06285v1)
  - Take notes on your own understanding of each section's architecture, to discuss in our next meeting.
    - Note any possible improvements to each section
    - Each team member should have a good understanding of the foundations of these papers, so that we can share with each other and plan how we will reproduce the results

- **In next week's meeting**, we should:

  - Share our findings on the papers, and ensure we all have a solid understanding
  - Create a plan and action items in a GitHub Project for the following 4 weeks, where we can continue to track to-do's
  - Plan how we will reproduce the paper results

### Meeting 1 - January 28th

- **We gone through the following items/key points:**

  - Interpretations of the two suggested papers and identified important model/tools used in their pipelines.
  - Improvements of steps in the pipelines were suggested (DynoV2, Clip4Str, collect more data (to increase domain) - possible approaches considered: manual collection/license plate), changing ResNet (leligility classifier) struture - increase number of layers, flipping numbers for legibility improvements, different Vit models

-  **For next week**, each team member must:

  - Clone and setup repo provided in the _A General Framework for Jersey Number Recognition in Sports Video_
  - Run and replicate the author's model
  - Play and understand as much of the the code as possible

- **In next week's meeting**, we should:

  - Continue discussion on possible improvements
  - Share findings we have upon running codes on our machine

- **Questions to ask the professor/TA:**

  - If using data collectly externally to fine-tune the model is allowed.
  - How much importance should we place on efficiency for improvement score. 

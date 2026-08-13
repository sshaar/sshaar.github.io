#!/usr/bin/env python3
"""Build public/cvpr2026-all.json: exhaustive catalog of every CVPR 2026 workshop
and every invited/keynote/panel speaker. Sources: official workshop pages (scraped
June 2026). Times are NOT included (most per-talk times are unpublished); this file
is a searchable catalog, complementary to the curated, timed cvpr2026-data.json.

Speaker tuples: (name, affiliation, talk_title_or_None, role)
"""
import json, os

# category key -> (label, color)
CATEGORIES = {
    "biometrics":      ("Biometrics", "#c2557a"),
    "vis-graphics":    ("Vision & Graphics", "#d98c5f"),
    "emerging":        ("Emerging Topics", "#8fd24f"),
    "synthesis":       ("Image & Video Synthesis / Generation", "#e06ab0"),
    "data":            ("Data / Synthetic Data", "#9aa14f"),
    "efficient":       ("Efficient / Edge / Scalable Vision", "#5fb0d9"),
    "architectures":   ("DL Architectures & Techniques", "#6f7fd9"),
    "accessibility":   ("Vision for Accessibility", "#4fb59a"),
    "generative":      ("Generative Models", "#d95f8c"),
    "foundation":      ("Foundation Models (LLM/VLM/VLA)", "#f0a830"),
    "vlr":             ("Vision, Language & Reasoning", "#b78bff"),
    "human":           ("Human Modeling & Understanding", "#d9a05f"),
    "embodied":        ("Embodied Vision & Robotics", "#737a87"),
    "affinity":        ("Affinity Groups", "#9a9a9a"),
    "medical":         ("Medical & Biological Vision", "#5fd97f"),
    "remote-sensing":  ("Photogrammetry & Remote Sensing", "#5f9ad9"),
    "detection":       ("Detection / Recognition / Segmentation", "#5fd9c2"),
    "robot-perception":("Robot Perception", "#8a92a0"),
    "explainable":     ("Explainable Computer Vision", "#c2a85f"),
    "driving":         ("Autonomous Driving", "#6f8a9a"),
    "comp-imaging":    ("Computational Imaging", "#5fc6d9"),
    "video":           ("Video: Action & Event Understanding", "#3fc6bd"),
    "3d":              ("3D from Multi-View & Sensors", "#7a82a0"),
    "applications":    ("Vision Applications & Systems", "#a0a05f"),
    "societal":        ("Vision for Societal Good", "#8fd24f"),
    "world-models":    ("World Models", "#9b8bff"),
    "multimodal":      ("Multimodal Learning", "#f0a830"),
    "safety":          ("Transparency / Safety / Fairness / Ethics", "#c25f5f"),
    "scene":           ("Scene Analysis & Understanding", "#7a9ad9"),
    "adversarial":     ("Adversarial Attack & Defense", "#c25f7a"),
    "open-world":      ("Open World Learning", "#5fa0c2"),
}

# Each workshop: (category, key, name, url, day, room, speakers, note)
# speakers: list of (name, affil, title, role)
W = []
def add(category, key, name, url, day, room, speakers, note=None):
    W.append({"category": category, "key": key, "name": name, "url": url,
              "day": day, "room": room, "speakers": speakers, "note": note})

# ---------------- Biometrics ----------------
add("biometrics","AeroHPR","AERO-HPR: Human Perception and Recognition in Aerial Surveillance","https://aero-hpr.github.io/",1,"110",[
 ("David Bolme","Oak Ridge National Laboratory","BRIAR Program Overview","invited"),
 ("David Cornett","Oak Ridge National Laboratory","BRIAR Program Overview","invited"),
 ("Arnold Wiliem","Shield AI, Australia","Tiny Objects, Big Questions: What Industry Needs from Future Vision Research","invited"),
 ("Pakpong Chirarattananon","University of Toronto","Advancing Miniature Aerial Robotics: Bio-Inspired Design and Mechanical Intelligence","invited"),
 ("Xiaoming Liu","UNC Chapel Hill","Algorithm Development in IARPA BRIAR program: Progress and Lessons Learned","invited"),
])
add("biometrics","SubtleVisual","2nd Workshop & Challenge on Subtle Visual Computing","https://sites.google.com/view/svc-cvpr26",1,None,[
 ("Essam Rashed","University of Hyogo",None,"keynote"),
 ("Mohamed Abouelenien","University of Michigan",None,"keynote"),
 ("Xin Liu","Google",None,"keynote"),
])
add("biometrics","FoundGenBio","Foundation and Generative Models in Biometrics","https://foundgen-bio.github.io/cvpr2026/",1,None,[
 ("Xiaoming Liu","UNC Chapel Hill",None,"invited"),
 ("Karthik Nandakumar","Michigan State University",None,"invited"),
])
add("biometrics","Biometrics2026","CVPR 2026 Biometrics Workshop","https://vislab.ucr.edu/Biometrics2026/index.php",2,None,[
 ("Alice O'Toole","University of Texas, Dallas","Face, Body, and Person Identification in Real-world Viewing Conditions","invited"),
 ("Kevin W. Bowyer","University of Notre Dame","How to Detect When the Probe in 1-to-N Facial ID is Out-of-Gallery","invited"),
],"Site redirects to ece.ucr.edu/workshop/biometrics-2026.")

# ---------------- Vision & Graphics ----------------
add("vis-graphics","AI4ContentCreation","AI for Content Creation","https://ai-for-content-creation.github.io",1,"610/612",[
 ("Rana Hanocka","University of Chicago","3D Generation and Editing","invited"),
 ("Alan Yuille","Johns Hopkins University","Building Representations","invited"),
 ("Christian Theobalt","Max-Planck-Institute for Informatics","4D Humans","invited"),
 ("Taesung Park","Reve","Controllable Image Generation","invited"),
 ("Saining Xie","New York University, AMI Labs","Representations and World Models","invited"),
])
add("vis-graphics","AI4VA","The 3rd AI for Visual Arts Workshop","https://ai4va-cvpr.github.io/",1,"Mile High 4AB",[
 ("Luba Elliott","Curator & Researcher, Creative AI",None,"keynote"),
 ("Hadar Averbuch-Elor","Cornell University & Cornell Tech",None,"keynote"),
 ("Ranjay Krishna","University of Washington & Allen Institute for AI",None,"keynote"),
 ("Pinar Yanardag","Virginia Tech",None,"keynote"),
])
add("vis-graphics","AI4Streaming","AI for Content Generation, Quality Enhancement and Streaming (AIGENS)","https://ai4streaming-workshop.github.io",1,"105",[
 ("Arturo Salmi","ARM","Neural Graphics in Real-time","invited"),
 ("Michael Stanway","The Compression Company","News in Neural Compression","invited"),
 ("Minguk Kang","Pika Labs","Real-time Video Generation as a Visual Interface for AI Agents","invited"),
 ("Kangle Deng","Roblox","Game Ready 3D Asset Generation","invited"),
 ("Ziteng Cui","University of Tokyo","RealX3D Benchmark","invited"),
 ("Jin Yeying","Tencent","Game World Model for Video Generation","invited"),
 ("Georgia Fargetta","University of Catania","Re-Anime600 - Novel Anime Dataset","invited"),
 ("Shuhong Liu","University of Tokyo","RealX3D Benchmark","invited"),
 ("Marcos V. Conde","University of Wurzburg","Implicit Neural Representations, Streaming, and More","invited"),
])
add("vis-graphics","WorldDifferentLight","See the World in a Different Light: Physical Appearance Modeling and Relighting","https://vcai.mpi-inf.mpg.de/projects/World-in-a-Different-Light/",2,"108",[
 ("Ira Kemelmacher-Shlizerman","University of Washington","Recent advances in data-driven and generative methods for Fashion AI","invited"),
 ("Hongzhi Wu","Zhejiang University","Differentiable acquisition jointly optimizing physical capture and computational reconstruction","invited"),
 ("Dor Verbin","Google DeepMind","Key bottlenecks in inverse rendering and generative priors","invited"),
 ("Zian Wang","Nvidia & University of Toronto","Video diffusion models for lighting and appearance in dynamic scenes","invited"),
 ("Shuang Zhao","UIUC","Physics-based differentiable rendering and inverse rendering","invited"),
 ("Shunsuke Saito","Meta","Moving beyond studio dome capture by leveraging in-the-wild data","invited"),
])
add("vis-graphics","APPX","Appearance Understanding and Generation","https://appx-workshop.github.io/",2,"4AB",[
 ("Shree Nayar","Columbia University","Computational photography and appearance modeling","invited"),
 ("Ravi Ramamoorthi","UCSD","Physics-based vision, rendering, and radiance field methods","invited"),
 ("Milos Hasan","NVIDIA Research","Material synthesis and inverse material estimation","invited"),
 ("Pieter Peers","College of William & Mary","Material capture, relighting, and appearance reproduction","invited"),
 ("Hongzhi Wu","Zhejiang University","SVBRDF datasets and high-fidelity material reconstruction","invited"),
 ("Zhao Dong","Meta Reality Labs","Reconstruction, differentiable rendering, and lighting models","invited"),
 ("Dor Verbin","Google DeepMind","Graphics-informed methods for understanding and synthesizing 3D scenes","invited"),
])

# ---------------- Emerging Topics ----------------
add("emerging","BitterLessons","Workshop on Bitter Lessons","https://sites.google.com/view/bitterlessonscv",1,"Four Seasons Ballroom 4",[
 ("Bill Freeman","MIT",None,"invited"),
 ("Vincent Sitzmann","MIT",None,"invited"),
 ("Dima Damen","University of Bristol",None,"invited"),
 ("Alyosha Efros","UC Berkeley",None,"invited"),
 ("Georgia Gkioxari","Caltech",None,"invited"),
 ("Evan Shelhamer","UBC",None,"invited"),
 ("Bharath Hariharan","Cornell",None,"invited"),
 ("Shenlong Wang","UIUC",None,"invited"),
 ("Jon Barron","Google",None,"invited"),
 ("Derek Hoiem","UIUC",None,"invited"),
])
add("emerging","MAPS","Multimodal Alignment for a Pluralistic Society","https://sites.google.com/view/maps-cvpr",1,None,[
 ("Ranjay Krishna","University of Washington; Allen Institute for AI",None,"invited"),
 ("David Ifeoluwa Adelani","McGill University; Mila",None,"invited"),
 ("Lora Aroyo","Google DeepMind",None,"invited"),
 ("Jason Stanley","ServiceNow Research",None,"invited"),
 ("Mohamed Elhoseiny","KAUST",None,"invited"),
 ("Maria Antoniak","University of Colorado Boulder",None,"invited"),
])
add("emerging","ReLearn","Rediscovering Intelligence: Can AI Still Learn from Humans? (ReLearn)","https://relearncvpr26.github.io/ReLearn/",1,"Mile High 4AB",[
 ("Alexei (Alyosha) Efros","UC Berkeley",None,"keynote"),
 ("Manling Li","Northwestern University","How Foundation Models Build (and Fail to Build) Spatial Minds: A Piagetian View","keynote"),
 ("Dima Damen","University of Bristol / Google DeepMind",None,"keynote"),
 ("Alan Yuille","Johns Hopkins University",None,"keynote"),
 ("Saining Xie","NYU Courant",None,"keynote"),
 ("William T. Freeman","MIT CSAIL / Google Research",None,"keynote"),
])
add("emerging","CV4Science","CV4Science: Using Computer Vision for the Sciences","https://sites.google.com/nyu.edu/computervisionforscience",2,"709",[
 ("Subhransu Maji","UMass Amherst",None,"invited"),
 ("Serena Yeung","Stanford University",None,"invited"),
 ("Bill Freeman","MIT",None,"invited"),
 ("Robert Jarolim","NASA High Altitude Observatory",None,"invited"),
 ("Hannah Kerner","Arizona State University",None,"invited"),
])

# ---------------- Image & Video Synthesis / Generation ----------------
add("synthesis","CVEU","AI for Creative Visual Content Generation, Editing and Understanding (CVEU)","https://cveu.github.io/",1,"501",[
 ("Soo Ye Kim","Adobe Research",None,"keynote"),
 ("Jack Parker-Holder","Google DeepMind",None,"keynote"),
 ("Amir Bar","FAIR",None,"keynote"),
 ("Mike Zheng Shou","National University of Singapore",None,"keynote"),
 ("Jiajun Wu","Stanford University",None,"keynote"),
])
add("synthesis","VideoWorldModels","1st Workshop on Video World Models: Interaction, Memory, and Efficiency","https://videoworldmodel-workshop.github.io/",1,"705/707",[
 ("Jack Parker-Holder","Google DeepMind",None,"invited"),
 ("Andrea Vedaldi","Oxford",None,"invited"),
 ("Sherry Yang","NYU / Google DeepMind",None,"invited"),
 ("Yilun Du","Harvard",None,"invited"),
 ("Xingang Pan","NTU",None,"invited"),
 ("Yaoyao Liu","UIUC",None,"invited"),
])
add("synthesis","LongVideoCreation","1st Workshop on AI-assisted Long Video Creation","https://bilibili.github.io/Index-anisora/cvpr_2026_workshop/index.html",1,"712",[
 ("Yaoyao Liu","UIUC","Enable Explicit 3D/4D Controls for Pre-trained Generative Models","invited"),
 ("Ismini Lourentzou","UIUC","Long-Form Video Generation Needs World Models","invited"),
 ("Pinar Yanardag","Virginia Tech","Leveraging Hidden Priors for Training-Free Control","invited"),
])
add("synthesis","J2A","Journey to the Awards: Generative AI for Movie-Grade Video Production (J2A)","https://cvpr26-j2a.github.io/",2,"Mile High 4CD",[
 ("Mateusz Malinowski","Moonvalley","From Text-to-Video to World Models","invited"),
 ("Ruben Villegas","Google DeepMind","Towards creating anything from any input","invited"),
 ("Chenlin Meng","Pika","From Research to Real-Time Creative Agents","invited"),
 ("Jimei Yang","Runway","Real-Time Video Generation and Editing for Creative Iteration","invited"),
 ("Wenqi Xian","Luma AI","From Prompting to Directing: Precision and Control in Video Generation","invited"),
 ("Kfir Aberman","Decart AI","Real-Time Video Models as Production Instruments","invited"),
 ("Jie Yang","Utopai Studios","Bridging Silicon Valley with Hollywood","invited"),
 ("Janne Kontkanen","Google DeepMind","Engineering for the Story: Research and Moviemaking","invited"),
 ("Ning Yu","Netflix","Towards Controllable Video Editing","invited"),
])

# ---------------- Data / Synthetic Data ----------------
add("data","DataCV","The 5th DataCV Workshop and Challenge","https://sites.google.com/view/datacv-2026-cvpr/",1,"710",[
 ("Tsui-Wei (Lily) Weng","UC San Diego",None,"invited"),
 ("Jason Alan Fries","Stanford University",None,"invited"),
 ("Ludwig Schmidt","Anthropic & Stanford University",None,"invited"),
])
add("data","AutoExpert","Auto-Annotation with Expert-Crafted Guidelines","https://autoexpert-arena.github.io/",1,"711",[
 ("James Hays","Georgia Tech",None,"invited"),
 ("Jason Corso","University of Michigan & Voxel51",None,"invited"),
 ("Pietro Perona","Caltech",None,"invited"),
 ("Subhransu Maji","University of Massachusetts",None,"invited"),
])
add("data","NeXD","Exploring the Next Generation of Data","https://sites.google.com/view/nexd26/home",2,"603",[
 ("Sanja Fidler","NVIDIA",None,"keynote"),
 ("Jia Deng","Princeton University",None,"keynote"),
 ("James Hays","Georgia Tech",None,"keynote"),
 ("Francesco Ferroni","NVIDIA",None,"keynote"),
 ("Ishan Misra","Meta",None,"keynote"),
 ("Bryan Wilder","Carnegie Mellon University",None,"keynote"),
 ("Despoina Paschalidou","NVIDIA",None,"keynote"),
])
add("data","SynData4CV","The 3rd Workshop on Synthetic Data for Computer Vision","https://syndata4cv.github.io/",2,"607",[
 ("Manling Li","Northwestern University",None,"invited"),
 ("Jia Deng","Princeton University",None,"invited"),
 ("Georgia Gkioxari","Caltech",None,"invited"),
 ("Andrew Owens","Cornell Tech",None,"invited"),
 ("Nupur Kumari","Carnegie Mellon University",None,"invited"),
])

# ---------------- Efficient / Edge / Scalable ----------------
add("efficient","EmbeddedVision","The 22nd Embedded Vision Workshop","https://embeddedvisionworkshop.wordpress.com/",1,"709",[
 ("Bowen Wen","NVIDIA Research","Building Foundation Models for Robotic Perception","invited"),
 ("Kang Eun Jeon","KAIST AI","One Model, Many Precisions: Flexible and Adaptive Compression for Edge Vision","invited"),
 ("Enzo Tartaglione","Telecom Paris","Bringing Training to the Edge: Subspace and Sparsity","invited"),
])
add("efficient","OnSensorVision","On Sensor Vision Workshop","https://onsensor-vision.github.io/",1,"Mile High 4EF",[
 ("Mika Laiho","Kovilta",None,"invited"),
 ("Mina Khoei","SynSense",None,"invited"),
 ("Gordon Wetzstein","Stanford University",None,"invited"),
 ("Kwabena Boahen","Stanford University",None,"invited"),
 ("Piotr Dudek","University of Manchester",None,"invited"),
 ("Barbara De Salvo","Meta Reality Labs Research",None,"invited"),
 ("Xuan 'Silvia' Zhang","Northeastern University",None,"invited"),
])
add("efficient","ECV","Efficient Deep Learning for Computer Vision","https://ecv-workshop.github.io/",1,"502",[
 ("Hai Li","Duke University","Intelligent Edge Computing","invited"),
 ("Xiaoyu Xiang","Meta","Efficient Image-to-3D Generation","invited"),
 ("Cagatay Bilgin","Meta","ExecuTorch: A Unified PyTorch Solution for On-Device ML","invited"),
 ("Ning Bi","Qualcomm","Agentic AI for the Edge","invited"),
 ("Song Han","MIT","Efficient Visual Generation on the Edge","invited"),
 ("An-Chieh Cheng","UC San Diego","Efficient Spatial Reasoning and Long-Horizon Planning","invited"),
 ("Oncel Tuzel","Apple","Advancing the Frontiers of On-Device AI","invited"),
 ("Zhijian Liu","UC San Diego","Efficient AI with Parallel Decoding, Quantization, and Sparsity","invited"),
])
add("efficient","EDGE","3rd Workshop on Efficient and On-Device Generation (EDGE)","https://cvpr26-edge.github.io/",1,"203",[
 ("Jack Parker-Holder","Google DeepMind","Genie 3 as a first step to open-ended world creation","invited"),
 ("Jiatao Gu","UPenn / Apple MLR","Are Normalizing Flows Good Candidates for Interactive World Models?","invited"),
 ("Zhuang Liu","Princeton University","Toward Practical Fully Open Generative Models","invited"),
 ("Stefano Ermon","Stanford University","Accelerating inference in diffusion models","invited"),
 ("Liang Zheng","ANU / Canva","DiffusionBench: Training, evaluating, and benchmarking T2I models","invited"),
 ("Han Cai","NVIDIA Research","Post-Training Acceleration for Efficient Diffusion Models","invited"),
 ("Oncel Tuzel","Apple","Advancing the Frontiers of On-Device AI","invited"),
 ("Lingjuan Lyu","Sony AI","Rethinking Foundation Models Beyond Scale","invited"),
 ("Chenfeng Xu","UT Austin / Together AI","Streaming Video Generation: From Pipelines to Operators","invited"),
])
add("efficient","MobileAI","Mobile AI workshop (6th edition)","https://ai-benchmark.com/workshops/mai/2026/",2,None,[
 ("Andrey Ignatov","AI Benchmark / ETH Zurich","Deploying Deep Learning Models on Mobile NPUs: What's New in 2026?","keynote"),
 ("Felix Baum","Qualcomm Technologies","A Practical Guide to Getting the DNN Accuracy You Need","keynote"),
])

# ---------------- DL Architectures ----------------
add("architectures","FedVision","The 5th Workshop on Federated Learning for Computer Vision (FedVision'26)","https://fedvision.github.io/fedvision2026/",1,"711",[
 ("Hao Wang","Stevens Institute of Technology",None,"keynote"),
 ("Liangqiong Qu","The University of Hong Kong",None,"keynote"),
 ("Ang Li","University of Maryland College Park",None,"keynote"),
])
add("architectures","NAS","Sixth Workshop on Neural Architecture Search","https://cvpr-nas.gitlab.io/workshop/website/index",1,None,[
 ("Rhea Sukthanker","University of Freiburg",None,"keynote"),
],"Only one keynote listed on the programme page.")
add("architectures","T4V","The 5th Workshop on Transformers for Vision and Multimodal AI (T4V)","https://sites.google.com/view/t4v-cvpr26/",1,"607",[
 ("Ranjay Krishna","University of Washington",None,"invited"),
 ("Jiatao Gu","UPenn / Apple",None,"invited"),
 ("Sherry Yang","NYU / Google DeepMind",None,"invited"),
 ("Juan Carlos Niebles","Salesforce / Stanford University",None,"invited"),
 ("Zhuang Liu","Princeton University",None,"invited"),
 ("Peter Tong","AMI Labs (NYU)",None,"invited"),
])
add("architectures","FGVC13","13th Workshop on Fine-grained Visual Categorization (FGVC)","https://sites.google.com/view/fgvc13/",1,"504",[
 ("Jeff Clune","University of British Columbia","The AI Scientific Revolution will be Driven by Open-Ended and AI-Generating Algorithms","invited"),
 ("David Rolnick","McGill University / Mila","Application-Driven Machine Learning for Biodiversity","invited"),
 ("Maria Antoniak","University of Colorado, Boulder","Classification for cultural analytics: A case study in storytelling","invited"),
 ("Morteza Karimzadeh","University of Colorado, Boulder","Location Encoders for Supervising Satellite-based Mapping","invited"),
])
add("architectures","DGEBF","Domain Generalization: Evolution, Breakthroughs, and Future Horizons (DG-EBF)","https://dg-ebf.github.io/2026/",2,"103",[
 ("Zsolt Kira","Georgia Tech",None,"invited"),
 ("Sara Beery","MIT",None,"invited"),
 ("Aditi Raghunathan","Carnegie Mellon University",None,"invited"),
 ("Kun Zhang","MBZUAI",None,"invited"),
 ("Abhinav Dhall","Monash University",None,"invited"),
 ("M. Saquib Sarfraz","Mercedes-Benz / KIT",None,"invited"),
])

# ---------------- Accessibility ----------------
add("accessibility","GenAI4SL","Generative AI for Sign Language (GenSign)","https://genai4sl.github.io/",1,"112",[
 ("Richard Bowden","University of Surrey & Signapse AI","AI Translation of Sign languages","keynote"),
 ("Colin Lea","Apple","Toward Fluent Sign Language AI: Moving Beyond Glosses","keynote"),
 ("Karen Livescu","Toyota Technological Institute at Chicago","A few steps toward understanding sign language in the real world","keynote"),
 ("Abraham Glasser","Gallaudet University","Sign Language AI: Towards Authentic Accessibility","keynote"),
])
add("accessibility","MSLR","2nd Workshop on Multimodal Sign Language Recognition (MSLR)","https://m-slrt.github.io/MSLR2026/",1,"210/212",[
 ("Gul Varol","Ecole des Ponts ParisTech",None,"invited"),
 ("Alex Lu","Microsoft Research",None,"invited"),
])
add("accessibility","VizWiz","VizWiz Grand Challenge Workshop","https://vizwiz.org/workshops/2026-vizwiz-grand-challenge-workshop/",2,"709",[
 ("Kate Saenko","Meta / Boston University","SAM 3: Segment Anything Model","invited"),
 ("Shaun Kane","Google Research","Disabled People & Disabled Data","invited"),
 ("Cordelia Schmid","INRIA","Grounded and Efficient Video Understanding","invited"),
 ("Ramin Ayanzadeh","University of Colorado Boulder","Parallel Lives Through the Same Eyes","invited"),
])

# ---------------- Generative Models ----------------
add("generative","GenXRID","Generative AI for XR and Identity-based Applications","https://bmdj-vt.github.io/workshops/cvpr_2026",1,None,[
 ("Adam Czajka","University of Notre Dame","True Lies: The Dual Nature of Synthetic Biometric Data","invited"),
 ("Karan Ahuja","Northwestern University & Google","Privacy-aware sensing for Contextual AI","invited"),
 ("Dillon Lohr","Meta","State of the Art in XR Eye-based Biometrics","invited"),
 ("Mingjun Li","University of Hartford","Motion Forecasting for VR Behavioral Biometrics","invited"),
 ("Mark Roman Miller","Illinois Institute of Technology","Motion, as read by Scientists, Machines, and Users","invited"),
])
add("generative","3D4Science","3D Geometry Generation for Scientific Computing (2nd Edition)","https://3d4sworkshop.github.io/",2,None,[
 ("Xiaoxiang Zhu","Technical University of Munich",None,"invited"),
 ("Tamar Shinar","UC Riverside","Reconstruction of implicit surfaces from fluid particles using CNNs","invited"),
 ("Ali Haddad","XRlabs","Physical AI in the Operating Room","invited"),
 ("Jiajun Wu","Stanford University","Seeing 4D Fluid Fields","invited"),
 ("Jeong Joon Park","University of Michigan","Beyond Neural Operators Towards Neural Solvers","invited"),
 ("Xiaoyu Xiang","Meta Reality Labs","Toward Interactable 3D World Generation","invited"),
 ("Danny Kaufman","Adobe Research","Multiscale Adaptive Simulation for Predictive Soft-Body Modeling","invited"),
 ("Chuang Gan","UMass Amherst / MIT-IBM Watson AI Lab","Building AI Agents with Physical Common Sense","invited"),
])
add("generative","LOVIF","1st Workshop on Low-Level Vision Frontiers with Generative AI (LOVIF)","https://lovif-cvpr2026-workshop.github.io/",2,"504",[
 ("Dimitris Samaras","Stony Brook University",None,"invited"),
 ("Robby T. Tan","National University of Singapore",None,"invited"),
 ("Chenyang Qi","Google",None,"invited"),
 ("Michael S. Brown","York University",None,"invited"),
])
add("generative","P13N","Personalization in Generative AI Workshop","https://p13n-workshop.github.io/",2,"4CD",[
 ("Pinar Yanardag","Virginia Tech",None,"keynote"),
 ("Kfir Aberman","Decart AI",None,"keynote"),
 ("Nataniel Ruiz","Google DeepMind",None,"keynote"),
 ("Or Patashnik","Tel Aviv University & Snap",None,"keynote"),
 ("Nupur Kumari","Carnegie Mellon University",None,"panel"),
 ("Hila Chefer","Black Forest Labs & Tel Aviv University",None,"panel"),
 ("Rana Hanocka","University of Chicago",None,"panel"),
])
add("generative","GenVision","4th Workshop on Generative Models for Computer Vision","https://generative-vision.github.io/workshop-CVPR-26/",2,"205",[
 ("Chelsea Finn","Stanford University",None,"invited"),
 ("Yilun Du","Harvard University","Visual Scene Understanding through Inverse Generative Modeling","invited"),
 ("Efstratios Gavves","University of Amsterdam","Physical World Models & Agents","invited"),
 ("Sherry Yang","NYU",None,"invited"),
 ("Georgia Gkioxari","Caltech","Beyond Image and Language: Building 3D Perception Systems","invited"),
 ("Matthias Niessner","TUM","3D Generative Models","invited"),
 ("Hila Chefer","Black Forest Labs","Is Scale All You Need? A Case for Native Generative-Representation Learning","invited"),
 ("Alan Yuille","Johns Hopkins University",None,"invited"),
])
add("generative","VidGenBenchEval","Video Generative Models: Benchmarks and Evaluation","https://vidgen-bench-eval.github.io/",2,"Mile High 3B",[
 ("Mike Zheng Shou","National University of Singapore","Video World Model for Robot Learning","keynote"),
 ("Yan Wang","NVIDIA Research","Alpamayo: Advancing Autonomous Driving With Reasoning VLA Models","keynote"),
 ("Yaoyao Liu","UIUC","Enable Explicit 3D/4D Controls for Pre-trained Generative Models","keynote"),
 ("Alan Bovik","University of Colorado Boulder","Two Experiments on the Perception of GenAI Pictures","keynote"),
 ("Zhuang Liu","Princeton University","Building and Evaluating Fully Open Generative Models","keynote"),
 ("Ming-Hsuan Yang","UC Merced & Google DeepMind","Toward World Models: Geometry, View Synthesis, and Visual Reasoning","keynote"),
 ("Jiajun Wu","Stanford University",None,"keynote"),
])
add("generative","GenRecon3D","1st Workshop on Generative 3D Reconstruction","https://genrecon3d.github.io/",2,"603",[
 ("Gordon Wetzstein","Stanford University",None,"keynote"),
 ("Katja Schwarz","World Labs",None,"keynote"),
 ("Christian Rupprecht","University of Oxford and ThirdDimension",None,"keynote"),
 ("Philipp Henzler","Google",None,"keynote"),
])
add("generative","GenAIStorytelling","2nd Workshop on GenAI for Storytelling (AISTORY)","https://aistory2026.github.io/",2,"105",[
 ("Yuchao Gu","NVIDIA","Breaking Efficiency Barriers in Large-Scale Video Diffusion Models","invited"),
 ("Kiyoharu Aizawa","University of Tokyo","How Humans Read Manga: Findings from User Studies","invited"),
 ("Chao Huang","University of Rochester / Tencent","Making Sound Part of the Story","invited"),
 ("Hideki Nakayama","University of Tokyo","Multidimensional Story Evaluation Toward Human-aligned Generation","invited"),
])

# ---------------- Foundation Models ----------------
add("foundation","GigaBrainChallenge","GigaBrain Challenge 2026: World Models Empowering VLA","https://gigaai-research.github.io/GigaBrain-Challenge-2026/",1,"506",[],
 "Challenge-format; no invited/keynote speakers listed (winning-team presentations).")
add("foundation","MUSI","The 2nd Workshop on Multimodal Spatial Intelligence (MUSI)","https://musi-workshop-2nd.github.io/",1,"601",[
 ("Katerina Fragkiadaki","Carnegie Mellon University",None,"keynote"),
 ("Angel X. Chang","Simon Fraser University",None,"keynote"),
 ("Chuang Gan","UMass Amherst / MIT-IBM Watson AI Lab",None,"keynote"),
 ("Roozbeh Mottaghi","Skild AI / University of Washington",None,"keynote"),
 ("Saining Xie","NYU / AMI Labs",None,"keynote"),
 ("Ranjay Krishna","University of Washington / Allen Institute for AI",None,"keynote"),
 ("Kristen Grauman","University of Texas at Austin",None,"keynote"),
])
add("foundation","AgenticVisualMedia","Workshop on Agentic AI for Visual Media","https://agentic-visual-media.github.io/",1,"Mile High 1EF",[
 ("Zhengzhong Tu","Texas A&M University","From Pixels to Systems: Agentic Visual Intelligence for Real-World CV","keynote"),
 ("Ranjay Krishna","University of Washington","From Vision to Action: Extracting Structure and Agency from Flat Pixels","keynote"),
 ("Xihui Liu","University of Hong Kong","Interactive and Multimodal Visual Generation towards World Models","keynote"),
 ("Christine Hu","Philo Labs","Agent and World, in One Model","keynote"),
 ("Jack Parker-Holder","Google DeepMind",None,"keynote"),
 ("Yeying Jin","Tencent","Game World Model","keynote"),
 ("Manling Li","Northwestern University","Failure Modes of VLM Agents: A Reinforcement Learning Perspective","keynote"),
])
add("foundation","VGI","Visual General Intelligence (VGI)","https://cvpr2026-vgi-workshop.limitlab.xyz/",1,"703",[
 ("Robert Geirhos","Google DeepMind","Are generative video models the path towards solving visual intelligence?","invited"),
 ("Aditi Raghunathan","Carnegie Mellon University","How to get creativity in AI","invited"),
 ("Matt Deitke","Meta Superintelligence Lab",None,"invited"),
 ("Kristen Grauman","University of Texas, Austin / Meta",None,"invited"),
 ("Yuki M. Asano","University of Technology Nuremberg","Learning from moving, Generalising from speaking","invited"),
 ("Andrea Vedaldi","University of Oxford / Meta","Building a 3D Foundation for Spatial AI","invited"),
 ("Alexei A. Efros","UC Berkeley","Surface Data vs. Deep Data: learning intelligence from the bottom up","invited"),
 ("Alex Kendall","Wayve","Frontier challenges to bring general purpose driving AI to 10M cars","invited"),
])
add("foundation","ThreeDLLMVLA","The 2nd 3D-LLM/VLA Workshop","https://3d-llm-vla.github.io/",1,"1CD",[
 ("Ziwei Liu","Nanyang Technological University",None,"keynote"),
 ("Yue Wang","University of Southern California",None,"keynote"),
 ("Leonidas Guibas","Stanford University",None,"keynote"),
 ("Angela Dai","Technical University of Munich",None,"keynote"),
 ("Ranjay Krishna","University of Washington",None,"keynote"),
 ("Marc Pollefeys","ETH Zurich",None,"keynote"),
])
add("foundation","DataMFM","DataMFM: Emerging Directions in Data for Multimodal Foundation Models","https://datamfm.github.io/",1,"111",[
 ("Ranjay Krishna","University of Washington",None,"invited"),
 ("Ziwei Liu","Nanyang Technological University",None,"invited"),
 ("Aishwarya Agrawal","University of Montreal / Mila",None,"invited"),
 ("Yilun Du","Harvard University",None,"invited"),
])
add("foundation","CVinW","The 5th Workshop on Computer Vision in the Wild (CVinW)","https://computer-vision-in-the-wild.github.io/cvpr-2026",2,None,[
 ("Manling Li","Northwestern University","Embodied Spatial Intelligence: Closing the Perception-Action Loop","invited"),
 ("Xiaolong Wang","UC San Diego",None,"invited"),
 ("Scott Yih","Meta FAIR","Say Less, Know More: Latent Representations and Procedural Retrieval","invited"),
 ("Kate Saenko","Boston University / Meta MSL","SAM3: Open-vocabulary object detection and segmentation","invited"),
 ("Chelsea Finn","Stanford University",None,"invited"),
 ("Mohit Bansal","UNC Chapel Hill","Memory, Action, and Skill Planning for Multimodal Agents","invited"),
 ("Jianfeng Gao","Microsoft",None,"panel"),
])
add("foundation","EvalGenFM","The Second Workshop on the Evaluation of Generative Foundation Models","https://evgenfm2026.github.io/",2,"Mile High 2C",[
 ("Ranjay Krishna","University of Washington","Updating generative evaluations to meet modern demands","invited"),
 ("Adriana Romero Soriano","Meta FAIR","Benchmarking and improving learning through imagination","invited"),
 ("Felix Friedrich","Black Forest Labs","Measure, then move the needle: safety across the multimodal pipeline","invited"),
 ("Yuxiong Wang","UIUC","Grounded or Delusional? Evaluating the Visual and Physical Reality of Foundation Models","invited"),
 ("Liangyan Gui","UIUC","Grounded or Delusional? (co-presented)","invited"),
 ("Sherry X. Chen","Motional","From Noisy Signals to Robust Evaluation","invited"),
 ("Koustuv Sinha","Meta FAIR",None,"invited"),
])
add("foundation","VidLLMs","2nd Workshop on Video Large Language Models","https://www.crcv.ucf.edu/cvpr2026-vidllms-workshop/",2,"3A-3D",[],
 "Invited Talks page not yet populated at scrape time.")
add("foundation","FMEmbodiedAgents","The 2nd CVPR Workshop on Foundation Models Meet Embodied Agents","https://foundation-models-meet-embodied-agents.github.io/cvpr2026/",2,"703",[
 ("Kristen Grauman","UT Austin",None,"invited"),
 ("Wei-Chiu Ma","Cornell University",None,"invited"),
 ("Xudong Wang","Physical Intelligence",None,"invited"),
 ("Kaichun Mo","NVIDIA",None,"invited"),
 ("An-Chieh Cheng","UC San Diego",None,"invited"),
])
add("foundation","ScaleBot","ScaleBot: First Workshop on Scalable Robot Learning Systems","https://scalebot-workshop.github.io/",2,"610/612",[
 ("Sergey Levine","UC Berkeley / Physical Intelligence",None,"invited"),
 ("Jason Ma","Dyna Robotics",None,"invited"),
 ("Wayne Wu","UCLA",None,"invited"),
 ("Chuan Wen","Shanghai Jiao Tong University",None,"invited"),
])
add("foundation","MMFM","The 5th Workshop on 'What is Next in Multimodal Foundation Models?' (MMFM)","https://mmfm-workshop.github.io/",1,"Four Seasons 4",[],
 "Invited Speakers section still a placeholder at scrape time.")
add("foundation","BigMAC","Big Model Adaptation In Computer Vision (BigMAC)","https://cvpr2026-bigmac-workshop.limitlab.xyz/",2,"Four Seasons 2",[
 ("Oriane Simeoni","Meta FAIR",None,"invited"),
 ("Christian Rupprecht","University of Oxford",None,"invited"),
 ("Cordelia Schmid","INRIA / Google",None,"invited"),
 ("Hilde Kuehne","University of Tuebingen / MIT-IBM Watson AI Lab",None,"invited"),
 ("Saining Xie","New York University",None,"invited"),
 ("Andrei Bursuc","valeo.ai / Inria",None,"invited"),
])

# ---------------- Vision, Language & Reasoning ----------------
add("vlr","GRAILV","GRAIL-V: Grounded Retrieval & Agentic Intelligence for Vision-Language","https://grailworkshops.github.io/",1,"506",[
 ("Dan Roth","University of Pennsylvania / Oracle AI","AI for Data and Data for AI","invited"),
 ("Kristen Grauman","University of Texas at Austin","Grounding Temporal Reasoning in Video Evidence","invited"),
 ("Scott Wen-Tau Yih","Meta","MetaCLIP: Open, Scalable Data Curation for Vision-Language Models","invited"),
 ("Mohit Bansal","UNC Chapel Hill","Long-Horizon Video Reasoning and Generation","invited"),
 ("Sujith Ravi","Oracle AI","Panel moderator","panel"),
 ("Vijay Krishnan","Turing",None,"panel"),
 ("Kenneth Marino","University of Utah",None,"panel"),
 ("Ming-Hsuan Yang","UC Merced / Google DeepMind",None,"panel"),
])
add("vlr","VAR","Workshop on Vision-based Assistants in the Real-World (VAR)","https://varworkshop.github.io/",1,None,[
 ("Katerina Fragkiadaki","Carnegie Mellon University",None,"invited"),
 ("Wenhu Chen","University of Waterloo",None,"invited"),
 ("Michael S. Ryoo","DeepMind / Stony Brook University",None,"invited"),
 ("Ziwei Liu","Nanyang Technological University",None,"invited"),
 ("Yao Qin","UC Santa Barbara",None,"invited"),
 ("Vicente Ordonez-Roman","Rice University",None,"invited"),
])
add("vlr","CogVL","Cognitive Foundations for Multimodal Models (CogVL)","https://cogvl.github.io/",1,"610/612",[
 ("Katerina Fragkiadaki","Carnegie Mellon University",None,"keynote"),
 ("Judith E. Fan","Stanford University",None,"keynote"),
 ("Alane Suhr","UC Berkeley / BAIR",None,"keynote"),
 ("Trevor Darrell","UC Berkeley / BAIR",None,"keynote"),
])
add("vlr","ViSCALE","The 2nd Workshop on Test-time Scaling for Computer Vision (ViSCALE)","https://viscale.github.io/",1,"506",[
 ("Sergey Levine","UC Berkeley",None,"invited"),
 ("Yong Jae Lee","University of Wisconsin-Madison",None,"invited"),
 ("Ranjay Krishna","University of Washington",None,"invited"),
 ("Ziwei Liu","Nanyang Technological University",None,"invited"),
 ("Manling Li","Northwestern University",None,"invited"),
 ("Mahmoud Assran","Meta AI",None,"invited"),
])
add("vlr","KnowledgeMR","2nd Workshop on Knowledge-Intensive Multimodal Reasoning","https://knowledgemr-workshop.github.io/",2,"704/706",[
 ("Biwei Huang","UC San Diego","Causal World Models for the Next AI Paradigm","invited"),
 ("Xin (Eric) Wang","UC Santa Barbara","The Agentic AI Loop: From Human-Like Reasoning to Group-Evolving Agents","invited"),
 ("Paul Liang","MIT","Self-Evolving Multimodal AI","invited"),
 ("Jiatao Gu","UPenn & Apple","Reasoning in Continuous Space","invited"),
 ("Mengdi Wang","Princeton","LabOS: The AI-XR Co-Scientist That Sees and Works With Humans","invited"),
])
add("vlr","MAR","Multimodal Algorithmic Reasoning Workshop (MAR)","https://marworkshop.github.io/cvpr26/",2,"601",[
 ("Juan Carlos Niebles","Salesforce AI Research",None,"keynote"),
 ("Jiayuan Mao","University of Pennsylvania","Learning, Reasoning, and Planning with Neuro-Symbolic Concepts","keynote"),
 ("Melanie Mitchell","Santa Fe Institute","Six Principles for Evaluating Cognitive Capabilities in AI Models","keynote"),
 ("Jialong Wu","Tsinghua University","Bridging World Models and Multimodal Reasoning","keynote"),
])
add("vlr","VisualConcepts","Workshop on Visual Concepts","https://sites.google.com/stanford.edu/visual-concepts-workshops",2,"501",[
 ("Niloy J. Mitra","University College London",None,"invited"),
 ("Judith Fan","Stanford University",None,"invited"),
 ("Yilun Du","Harvard University",None,"invited"),
 ("Ranjay Krishna","University of Washington",None,"invited"),
 ("Qianqian Wang","Harvard University",None,"invited"),
 ("Yael Vinker","MIT",None,"invited"),
])
add("vlr","MMRAGI","The 2nd Workshop on Multi-Modal Reasoning for Agentic Intelligence (MMRAGI)","https://mmragi.github.io/mmragi/",2,"3A",[
 ("Yunzhu Li","Columbia University","Foundation Models for Robotic Manipulation","invited"),
 ("Alexander Toshev","Apple ML Research","Reasoning Agents for the Digital World","invited"),
 ("Biwei Huang","UC San Diego","Causal World Models for the next AI Paradigm","invited"),
 ("Kristen Grauman","University of Texas at Austin","Grounding Video Reasoning in Visual Evidence","invited"),
 ("Ranjay Krishna","University of Washington","It is Time to Rethink Grounding","invited"),
])

# ---------------- Human Modeling & Understanding ----------------
add("human","HuMoGen","The 3rd Workshop on Human Motion Generation (HuMoGen)","https://humogen.github.io/",1,"505",[
 ("Gul Varol","Ecole des Ponts ParisTech","From Bodies to Hands: Language-Guided 3D Motion Generation","invited"),
 ("Libin Liu","Peking University","Revisiting Linear Policies for Whole-Body Motion Control","invited"),
 ("Christian Theobalt","Max-Planck Institute for Informatics","Digital Avatars: Modeling and Simulation","invited"),
 ("Alexander Richard","Reality Labs Research @ Meta","Towards Embodied Social Agents in XR","invited"),
 ("Sebastian Starke","Meta Reality Labs","AI4AnimationPy: An Open-Source Framework for Character Animation Research","invited"),
])
add("human","P3HA","2nd Workshop on Photorealistic 3D Head Avatars","https://kaldir.vc.cit.tum.de/nersemble_benchmark/cvpr2026",1,"107",[
 ("Timo Bolkart","Google Zurich","Semantic Correspondence: From Meshes to Gaussian Avatars","invited"),
 ("Javier Romero","Meta Codec Avatar Lab","Are human representations already bitter enough?","invited"),
 ("Juyong Zhang","University of Science and Technology of China","Photo-realistic 3D Head Avatars","invited"),
 ("Vanessa Sklyarova","Max Planck ETH Center for Learning Systems","Modeling Strand-based Hairstyles for Digital Human Avatars","invited"),
 ("Zhuo Su","ByteDance","Towards Deployable 3D Avatars","invited"),
 ("Christian Theobalt","Max Planck Institute for Informatics","Highly Realistic Human Reconstruction and Rendering","invited"),
])
add("human","ABAW","10th Affective & Behavior Analysis in-the-wild (ABAW)","https://affective-behavior-analysis-in-the-wild.github.io/10th",1,None,[
 ("Zheng Lian","Tongji University",None,"keynote"),
 ("Siyang Song","University of Exeter",None,"keynote"),
 ("Bo Wang","University of Mississippi",None,"keynote"),
])
add("human","CVBW","Computer Vision for Biomechanics Workshop","https://cvbw2026.github.io/",1,"112",[
 ("R. James Cotton","Northwestern University",None,"keynote"),
 ("Scott Uhlrich","University of Utah",None,"keynote"),
 ("Patrick Lucey","Stats Perform",None,"keynote"),
 ("Marilyn Keller","Max Planck Institute for Intelligent Systems",None,"keynote"),
 ("Clinton Fookes","BiomotionAI",None,"panel"),
 ("Akila Hewa Thondilege","BiomotionAI",None,"panel"),
])
add("human","MOMA","Workshop on Multimodal Human Motion Analysis","https://www.iit.it/en/web/hrii/cvpr2026-workshop",1,"601",[
 ("Kristen Grauman","University of Texas at Austin","From Novice to Expert: Analyzing Skilled Human Activity in Video","keynote"),
 ("Jianfei Yang","Nanyang Technological University","Multimodal Foundation Model for Language-Grounded Human Sensing","keynote"),
 ("Ronald Poppe","Utrecht University","Temporal Coordination in Fine-Grained Analysis of Parent-Child Interactions","keynote"),
 ("Thomas Ploetz","Georgia Institute of Technology","Sensor-Based Human Activity Recognition for Health and Wellbeing","keynote"),
 ("Suining Henry He","University of Connecticut","Human-Mobility Interaction: A Multimodal Tale of Micromobility","keynote"),
])
add("human","CV4CHL","2nd Workshop on Computer Vision for Children","https://pediamedai.com/cv4chl/",2,"Exhibit Hall A 106",[
 ("Sanmi Koyejo","Stanford University","Do our vision systems actually work for children?","keynote"),
 ("Jean-Marc Odobez","Idiap Research Institute and EPFL","From Gaze Estimation to Child Interaction Understanding","keynote"),
 ("Dima Damen","University of Bristol and Google DeepMind","My World, My View - Learning from an Egocentric Perspective","keynote"),
 ("James M. Rehg","University of Illinois Urbana-Champaign","AI Models Facilitate Automated Measurement of Social Gaze","keynote"),
 ("Boqing Gong","Boston University",None,"panel"),
 ("Yu Tian","University of Central Florida",None,"panel"),
 ("Yapeng Tian","University of Texas at Dallas",None,"panel"),
])
add("human","HumansOfGenAI","Humans of Generative AI","https://humansofgenerativeai.github.io/",2,"710",[
 ("Juliana Castro Varon","The New York Times","What Is (and What Is Not) a Good Use of AI in Journalism?","keynote"),
 ("Rishi Bommasani","Stanford HAI","On Frontier AI and Jobs","keynote"),
 ("Tiana Oreglia","Concept Artist and Artist Advocate",None,"panel"),
 ("Elissa M. Redmiles","Georgetown University",None,"panel"),
 ("David A. Forsyth","University of Illinois at Urbana-Champaign",None,"panel"),
])
add("human","PhysHuman","PhysHuman: Physically Grounded Human Perception and Modeling","https://physhuman.github.io/",2,"110",[
 ("Jiajun Wu","Stanford University",None,"keynote"),
 ("Xin (Shane) Li","Texas A&M University",None,"keynote"),
 ("Christian Theobalt","MPI for Informatics",None,"keynote"),
 ("Ehsan Adeli","Stanford University",None,"keynote"),
 ("Dima Damen","University of Bristol & Google DeepMind",None,"keynote"),
])
add("human","HiGen","2nd Workshop on Human-Interactive Generation and Editing (HiGen)","https://higen-2025.github.io/",1,"109",[
 ("Enze Xie","NVIDIA","SANA-Video & World Model","invited"),
 ("Kristen Grauman","UT Austin","Envisioning Action: Generating Visual Futures for Instruction and Planning","invited"),
 ("Shuyang Sun","Google DeepMind","Vision Banana: Image Generators are Generalist Vision Learners","invited"),
 ("Jack Parker-Holder","Google DeepMind","Genie 3 as a First Step to Open-Ended World Creation","invited"),
 ("Jianming Zhang","Adobe","Foundation Models at Adobe","invited"),
 ("Maneesh Agrawala","Stanford University","Making is Decision Making","invited"),
 ("Shyamal Buch","Luma AI","Uni-1: A Unified Understanding and Generation Model","invited"),
 ("Jiajun Wu","Stanford University","Flexible Conditioning for Generating Diverse Human-Object Interactions","invited"),
 ("Haoqi Fan","Bytedance Seed",None,"invited"),
],"Workshop spans June 3-4.")
add("human","GazeWorkshop","The 7th International Workshop on Eye and Gaze in Computer Vision","https://gazeworkshop.github.io/2026/",2,"711",[
 ("James M. Rehg","University of Illinois Urbana-Champaign","Inference and Forecasting of 2D and 3D Gaze","keynote"),
 ("Ken Pfeuffer","Aarhus University","Eye-Hand Symbiosis","keynote"),
])

# ---------------- Embodied Vision & Robotics ----------------
add("embodied","IPA","IPA: Interactive Physical AI Workshop","https://research.nvidia.com/labs/amri/projects/IPA/2026/",1,"203",[
 ("Alexander Richard","Meta","Towards Embodied Social Agents in XR","keynote"),
 ("Agon Serifi","Disney Research Robotics","From Human Motion to Robot Behavior","keynote"),
 ("Maja Mataric","USC; Google DeepMind","The Challenges of Human-Centered AI and Robotics","keynote"),
])
add("embodied","ActiVis","Bridging Vision, Language, and Action (ActiVis)","https://activis-workshop.github.io/",1,"503",[
 ("Saurabh Gupta","University of Illinois Urbana-Champaign",None,"invited"),
 ("Ming-Yu Liu","NVIDIA Research",None,"invited"),
 ("Nathan F. Lepora","University of Bristol",None,"invited"),
 ("Yunzhu Li","Columbia University",None,"invited"),
 ("Chelsea Finn","Stanford University",None,"invited"),
 ("Ruoshi Liu","Amazon Frontier AI & Robotics (FAR)",None,"invited"),
 ("Marco Pavone","Stanford University",None,"invited"),
])
add("embodied","EmbodiedInTheWild","From Lab Demos to Daily Tasks: Embodied Intelligence in the Wild","https://opendrivelab.com/cvpr2026/workshop",1,"Four Seasons 1",[
 ("Hao Su","Fudan University","The Illusion of Physical Understanding","keynote"),
 ("Zhiyu Huang","UCLA","nuReasoning: Advancing Reasoning-Centric Autonomous Driving","keynote"),
 ("Jiahui Lei","UC Berkeley","World Motion Model, from 4D Vision to Robotics and Beyond","keynote"),
 ("Yilun Du","Harvard University","Embodied Intelligence with World Models","keynote"),
 ("Rika Antonova","University of Cambridge","Advancements in Mobile Manipulation, Sensing, and Shape Adaptation","keynote"),
 ("Jiatao Gu","University of Pennsylvania","Should Embodied Intelligence Care About 3D?","keynote"),
])
add("embodied","SenseOfSpace","Sense of Space: Multi-Sensory Modeling for Embodied Intelligence","https://sense-of-space.github.io/",1,"Mile High 2C",[
 ("Nima Fazeli",None,"Tactile Intelligence: Learning to Perceive and Act through Touch","keynote"),
 ("Mahi Shafiullah",None,"Are robots slowing down robotics?","keynote"),
 ("Marc Pollefeys",None,None,"keynote"),
 ("Wojciech Matusik","MIT CSAIL",None,"keynote"),
 ("Homanga Bharadhwaj",None,"Observational Learning for Manipulation via Visual Imitation of Humans","keynote"),
 ("Boyi Li",None,"Learning Multimodal Robot Policies with Generative Signals","keynote"),
 ("Sha Yi",None,"When is touch necessary for robotics?","keynote"),
 ("Lingjie Liu",None,None,"keynote"),
 ("Paul Liang",None,"Expanding AI's Senses: Touch, Smell, and Beyond","keynote"),
 ("Ismini Lourentzou",None,None,"panel"),
 ("Christian Theobalt",None,None,"panel"),
])
add("embodied","MARS","1st Workshop on Multi-Agent Robotic Systems (MARS)","https://mars-eai.github.io/CVPR-SCI-MARS-Webpage/",1,"Mile High 4EF",[
 ("Dhruv Shah","Google DeepMind",None,"keynote"),
 ("Xihui Liu","The University of Hong Kong",None,"keynote"),
 ("Shanghang Zhang","Peking University",None,"keynote"),
 ("Wenlong Huang","Stanford University",None,"keynote"),
])
add("embodied","EmbodiedReasoning","Embodied Reasoning in Action","https://embodied-reasoning.github.io/",2,"605",[
 ("Furong Huang","University of Maryland","From Perception to Action: Latent World Models to State-Aware Scene Graphs","invited"),
 ("Ranjay Krishna","University of Washington / Ai2","MolmoAct2: Making Open Robotics Reasoning Models","invited"),
 ("Tianmin Shu","Johns Hopkins University","Online World Modeling for Closed-Loop Planning","invited"),
 ("Cheng Chi","Beijing Academy of Artificial Intelligence","Embodied Reasoning for Robotic Manipulation","invited"),
 ("Boyi Li","NVIDIA","FoundationMotion: Auto-Labeling and Reasoning about Spatial Movement in Videos","invited"),
 ("Jiajun Wu","Stanford University","Embodied Reasoning via Spatial-Temporal Representations","invited"),
 ("Karl Pertsch","Physical Intelligence",None,"invited"),
 ("Yilun Du","Harvard University","Embodied Reasoning with World Models","invited"),
])
add("embodied","4DDT","4D Digital Twins: Real-to-Sim-to-Real for Physical AI","https://research.nvidia.com/labs/amri/projects/4DDT/2026/",2,"2C",[
 ("Katerina Fragkiadaki","Carnegie Mellon University","Learning Persistent 4D World Models from Video","keynote"),
 ("Hanbyul Joo","Seoul National University","Learning Robot Skills from Human Demonstrations Without 3D Motion Capture","keynote"),
 ("Francis Williams","NVIDIA","fVDB: A Framework for Sparse, Large-Scale Spatial Intelligence","keynote"),
 ("Gordon Wetzstein","Stanford University","From World Models to World Agents","keynote"),
 ("Xueyan Zou","Tsinghua University","Actionable World Representation","keynote"),
])
add("embodied","EmbodiedAI","The Seventh Annual Embodied Artificial Intelligence Workshop","https://embodied-ai.org/",2,"107",[
 ("Baoxiong Jia","BIGAI","Understand the 3D World for Humanoid Robots","invited"),
 ("Stefan Leutenegger","ETH Zurich","Spatial AI and Robot Learning for the Real World","invited"),
 ("Lewis Chiang","Google DeepMind",None,"invited"),
 ("Ruiqi Gao","Google DeepMind","World Models for Embodied AI","invited"),
 ("Tapomayukh Bhattacharjee","Cornell University","Long-Horizon Embodied AI","invited"),
 ("Yilun Du","Harvard","World Models for Robot Manipulation and Planning","invited"),
 ("Jiaolong Yang","Microsoft Research Asia","3D Computer Vision and Spatial AI","invited"),
 ("Sarah Parisot","Microsoft Research Cambridge","Building World Models for Creative Use","invited"),
 ("Dinesh Jayaraman","UPenn GRASP Lab","World Models for Robot Learning","invited"),
 ("Anthony Francis","Logical Robotics","Long-Horizon Safety in Embodied AI","panel"),
])

# ---------------- Affinity Groups ----------------
add("affinity","LatinXinCV","LatinX in Computer Vision Research Workshop","https://www.latinxinai.org/cvpr-2026",1,"106",[
 ("Paula Ramos","NVIDIA","How to Understand Physical AI and World Foundation Models","keynote"),
 ("Murilo Gustineli","Voxel51; Georgia Tech","Building a Culture of Applied Research: The DS@GT ARC Story","keynote"),
])
add("affinity","WiCV","Women in Computer Vision (WiCV)","https://sites.google.com/view/wicv-cvpr-2026/",1,"708",[
 ("Cordelia Schmid","Inria / Google",None,"keynote"),
 ("Sanja Fidler","NVIDIA / University of Toronto",None,"keynote"),
 ("Georgia Gkioxari","Caltech",None,"keynote"),
 ("Sarah Parisot","Microsoft Research Cambridge",None,"keynote"),
 ("Katie Bouman","Caltech",None,"keynote"),
],"Katie Bouman per web search; not confirmed on speakers page snapshot.")

# ---------------- Medical & Biological ----------------
add("medical","MMFMBiomed","Multimodal Foundation Models for Biomedicine","https://mmfm-biomed.github.io/",1,"1CD",[
 ("James Zou","Stanford University","Learning the language of sleep and the Virtual Biotech","invited"),
 ("Emily Fox","Stanford University","Unraveling Disease: How Do We Learn Causality in Drug Discovery?","invited"),
 ("Maria Brbic","EPFL","Multimodal Generative Modeling of Cellular Complexity","invited"),
 ("Mengdi Wang","Princeton University","LabOS: The AI-XR Co-Scientist That Sees and Works With Humans","invited"),
])
add("medical","FMV","The 3rd Workshop on Foundation Models for Medical Vision (FMV)","https://fmv-cvpr26workshop.github.io/",1,"607",[
 ("Jakob Nikolas Kather","Technical University Dresden","AI applications in oncology and cancer research","invited"),
 ("Faisal Mahmood","Harvard Medical School","Multimodal and Generative AI for Pathology","invited"),
 ("Hoifung Poon","Microsoft","Toward Virtual Patient: AI for Accelerating Medical Discovery","invited"),
 ("Pranav Rajpurkar","Harvard Medical School","Routing to Autonomous AI for Medicine","invited"),
])
add("medical","PHAROS","PHAROS AI Factory for Medical Imaging & Healthcare","https://ai-medical-image-analysis.github.io/6th",1,None,[
 ("Anastasia Chatzidimitriou","INAB | CERTH, Greece","Identifying real-world patterns for patient journeys (OMOP-CDM)","keynote"),
 ("Pantelis Natsiavas","INAB | CERTH, Greece","Identifying real-world patterns for patient journeys (OMOP-CDM)","keynote"),
])
add("medical","MCV","12th Workshop on Medical Computer Vision (MCV)","https://sites.google.com/view/cvpr2026mcv",1,"605",[
 ("Dimitris N. Metaxas","Rutgers University","Explainability, Generation, Physics and Dynamics in ML for Biomedical Applications","keynote"),
 ("Daguang Xu","NVIDIA","Driving AI Innovation in Healthcare through Open Data and Foundation Models","keynote"),
 ("Sharon X. Huang","Penn State University","Advancing Diagnostic Robustness and Privacy-Preserving Model Training","keynote"),
 ("Mathias Unberath","Johns Hopkins University","Digital Twins for Ambient and Embodied Surgical AI","keynote"),
 ("Archana Venkataraman","Boston University","Lightweight and Interpretable AI as a New Window into Brain Dysfunction","keynote"),
 ("Maddie Traverse","Google","MedGemma: an open vision-language model for diverse medical applications","keynote"),
 ("Hoifung Poon","Microsoft Research","Learning the Language of Patients","keynote"),
 ("Jeremias Sulam","Johns Hopkins University","Flexible methods for uncertainty quantification in medical imaging","keynote"),
 ("Kayhan Batmanghelich","Boston University","Image-Text Foundational for Volumetric Image","keynote"),
 ("Ehsan Adeli","Stanford University","From Bedside to Living Room: Reimagining Care Through Ambient Intelligence","keynote"),
 ("Mert R. Sabuncu","Cornell University","Prevalence Adjustment as a Way to Handle Distribution Shift in Medical Vision","keynote"),
 ("Rene Vidal","University of Pennsylvania","Trustworthy AI in Health: Foundation Models for Radiology, Cardiology and Autism","keynote"),
])
add("medical","CVMI","11th Workshop on Computer Vision and Multimodal Microscopy Image Analysis (CVMI)","https://cvmi-workshop.github.io/index.html",None,None,[
 ("Daguang Xu","NVIDIA","Multimodal AI for Healthcare Development","invited"),
 ("Alex Beatson","Axiom Bio","Vision Transformers for Drug-Induced Toxicity and Mechanism Prediction","invited"),
 ("Olivier Gevaert","Stanford University","Multi-modal modeling in precision medicine","invited"),
 ("Eran Hornstein","Weizmann Institute of Science","NOVA: Scalable Vision Foundation Model for Organellome-Wide Phenotyping","invited"),
 ("Michelle Chan","Princeton University","Learning Multi-Modal Tissue Representations","invited"),
 ("Vivek Gopal Ramaswamy","UCSF Gladstone Institutes","The Thinking Microscope","invited"),
])
add("medical","MedReasoner","Medical Reasoning with Vision Language Foundation Models","https://med-reasoner.github.io/cvpr2026",2,"110",[
 ("Hoifung Poon","Microsoft Research",None,"invited"),
 ("Faisal Mahmood","Harvard University",None,"invited"),
 ("Tanishq Mathew Abraham","Sophont",None,"invited"),
 ("Serena Yeung","Stanford University",None,"invited"),
 ("Maria Xenochristou","Amazon Health Services",None,"invited"),
])
add("medical","CV4Clinical","Bridging AI and Medical Reality (CV4Clinical)","https://cv4clinical.github.io/cv4clinical_2026/",2,"Mile High 1AB",[
 ("Bernhard Kainz","FAU Erlangen Nurnberg and Imperial College London","From Concept to Clinic","keynote"),
 ("Le Lv","Ant Group","Cross-modality and Multi-modality Learning for Medical Imaging","keynote"),
 ("Siqi Liu","Tempus AI","Foundation Models for Cancer Precision Medicine","keynote"),
 ("You Zhang","UT Southwestern Medical Center","Self-Supervised Methods for Time-Resolved Tomographic Imaging","keynote"),
])

# ---------------- Remote Sensing ----------------
add("remote-sensing","MORSE","The Second Workshop on Foundation and Large Vision Models in Remote Sensing (MORSE)","https://sites.google.com/view/cvpr-morse/",None,None,[
 ("David Rolnick","McGill University / Mila",None,"keynote"),
 ("Sylvain Lobry","Universite Paris Cite (LIPADE)",None,"keynote"),
 ("Abhijit Mahalanobis","University of Arizona",None,"keynote"),
 ("Mikhail Klassen","Planet",None,"keynote"),
])
add("remote-sensing","MONTI","1st Workshop on Monitoring the World through an Imperfect Lens (MONTI)","https://sites.google.com/view/monti2026/home",1,"105",[
 ("Johannes Jakubik","IBM",None,"invited"),
 ("Ritwik Gupta","University of Maryland",None,"invited"),
 ("Hannah Kerner","Arizona State University",None,"invited"),
 ("Nico Lang","University of Copenhagen",None,"invited"),
 ("Morteza Karimzadeh","University of Colorado",None,"invited"),
])
add("remote-sensing","EarthVision","EarthVision: Large Scale CV for Remote Sensing","https://www.grss-ieee.org/events/earthvision-2026/",2,"507",[
 ("Caleb Robinson","Microsoft AI for Good Research Lab","From local to global maps from satellite imagery","keynote"),
 ("Esther Rolf","University of Colorado, Boulder","Simple ideas with big impacts in CV for Earth Observation","keynote"),
])

# ---------------- Detection / Recognition / Segmentation ----------------
add("detection","PBVS","22nd Workshop on Perception Beyond the Visible Spectrum (PBVS)","https://pbvs-workshop.github.io/index.html",1,None,[
 ("Brian Sheil","University of Cambridge","Multi-Modal Sensing for Surface and Subsurface Infrastructure","keynote"),
 ("Sarah Parisot","Microsoft","Building World Models for Creative Use","keynote"),
 ("Daniel Cremers","Technical University of Munich","From LSD-SLAM to ViSTA-SLAM","keynote"),
])
add("detection","VisionInspection","4th Workshop on Vision Based Industrial Inspection","https://vision-workshop-26.github.io/cvpr-2026/",1,"205",[
 ("Paul Shahidi","Anduril Industries","Why Most Industrial Vision Systems Fail their First Deployment","invited"),
 ("Jennifer Vandoni","Safran","AI for Non-Destructive Testing and Material Characterization in Aerospace","invited"),
 ("Dan Cristian Dinca","Rapiscan Systems","Intelligent Security Screening (X-ray)","invited"),
 ("Charles A. Bouman","Purdue University","Past, Present, and Future Methods for Sparse View CT","invited"),
 ("Salman Khan","MBZUAI","Towards Generalist and Edge Intelligence for Industrial Inspection","invited"),
 ("Amir Afrasiabi","The Boeing Company","Self-Validating Augmented Reality Using Artificial Intelligence","invited"),
])

# ---------------- Robot Perception ----------------
add("robot-perception","WMAS","Workshop on World Models Meet Active Sensing and Closed-Loop Planning","https://cvpr26wmas.github.io/",1,"Mile High 2A",[
 ("Nicholas Roy","MIT CSAIL","World Models and Why We Should Care about Their Structure","invited"),
 ("Alan Yuille","Johns Hopkins University","World Models: Bayes or Bust?","invited"),
 ("Yiannis Aloimonos","University of Maryland","Generative Action Systems","invited"),
 ("Chelsea Finn","Stanford University & Physical Intelligence","Evaluating and Improving Robotic Foundation Models with World Models","invited"),
])
add("robot-perception","URVis","Unified Robotic Vision with Cross-Modal Sensing and Alignment (URVis)","https://urvis-workshop.github.io/",2,"4AB",[
 ("Ismini Lourentzou","UIUC","From VLAs to World Action Models","invited"),
 ("Cornelia M. Fermuller","University of Maryland",None,"invited"),
 ("Hildegard Kuhne","University of Tubingen","Grounded Perception for Robotics","invited"),
 ("Yeying Jin","Tencent","Game World Model","invited"),
 ("Felix Heide","Princeton & Torc Robotics","Robot Learning with a 1000m Horizon","invited"),
 ("Ranjay Krishna","University of Washington & AI2","Reasoning models for Robotics","invited"),
])
add("robot-perception","MaCVi","4th Workshop on Maritime Computer Vision (MaCVi)","https://macvi.org/workshop/cvpr",2,"Mile High 1AB",[
 ("Fiona Hua","Einride","From Sea to Street: What Maritime Autonomy Can Learn from Large-Scale AV Deployment","keynote"),
 ("Parneet Kaur","Einride","From Sea to Street (co-presented)","keynote"),
 ("Marek Suchowski","catskill GmbH","AIS in the Wild: Coverage Gaps, Spoofing, and What CV Models Must Know","keynote"),
])

# ---------------- Explainable CV ----------------
add("explainable","XAI4CV","The 5th Explainable AI for Computer Vision (XAI4CV) Workshop","https://xai4cv-workshop.github.io/xai4cv2026/",1,"Mile High 1AB",[
 ("Chaofan Chen","University of Maine","Learning by Comparison: Case-based Reasoning for Interpretable Vision Models","invited"),
 ("Anh Totti Nguyen","Auburn University","Vision Language Models with Explainable Bottleneck Layers","invited"),
 ("Elizabeth Barnes","Boston University","Training Dynamics as a Form of XAI","invited"),
 ("Maximilian Dreyer","Fraunhofer Heinrich Hertz Institute","From Concepts to Control: Diagnosing and Steering Vision Foundation Models","invited"),
])
add("explainable","HOW","How Do Vision Models Work? (HOW)","https://sites.google.com/view/how-cvpr-workshop",2,"Mile High 1EF",[
 ("Jaden Fiotto-Kaufman","NDIF","NDIF tutorial: Toward a Shared Stack for Vision Interpretability","invited"),
 ("Thomas Fel","Goodfire","Neural Geometry in Large Vision Models","invited"),
 ("Dana Arad","Technion","Through Layers and Tokens: Tracing Information Flow","invited"),
 ("Alexei Efros","UC Berkeley",None,"invited"),
 ("Tsui-Wei (Lily) Weng","UCSD","Toward a Science of Interpretability","invited"),
 ("Zhuang Liu","Princeton","How Do Vision Models Learn to Reason?","invited"),
])

# ---------------- Autonomous Driving ----------------
add("driving","AUTOPILOT","AUTOPILOT: Autonomous Understanding Through Open-world Perception","https://www.autopilot-cvpr.net/",1,"Hall 3A",[
 ("Jose M. Alvarez","NVIDIA",None,"keynote"),
 ("Manmohan Chandraker","UC San Diego / NEC Labs America",None,"keynote"),
 ("Matthew Alun Brown","Wayve",None,"keynote"),
 ("Bat El Shlomo","ZOOX",None,"keynote"),
])
add("driving","DriveX","Foundation Models for Autonomous Driving (DriveX)","https://drivex-workshop.github.io/cvpr2026",1,"207",[
 ("Walter Zimmer","UCLA & TUM","Opening Keynote (cooperative roadside-vehicle perception via V2X)","keynote"),
 ("Balajee Kannan","Motional",None,"keynote"),
 ("Angela Dai","Technical University of Munich",None,"keynote"),
 ("Mingxing Tan","Waymo","Waymo World Model","keynote"),
 ("Matthew Brown","Wayve",None,"keynote"),
 ("Akshay Gopalkrishnan","Nomadic AI",None,"keynote"),
 ("Marco Pavone","Stanford & NVIDIA",None,"keynote"),
 ("Phil Duan","Tesla",None,"keynote"),
 ("Tony Qi","Motional","Challenge keynote (nuReasoning dataset)","keynote"),
 ("Manmohan Chandraker","UCSD & NEC Labs",None,"keynote"),
 ("Jiaqi Ma","UCLA",None,"keynote"),
 ("Holger Caesar","Delft University",None,"keynote"),
 ("Daniel Cremers","TUM",None,"keynote"),
 ("Daniel Watzenig","Graz University","Sponsor announcements keynote","keynote"),
])
add("driving","WAD","Workshop on Autonomous Driving (WAD)","https://cvpr2026.wad.vision/",1,"603",[
 ("Holger Caesar","TU Delft","Autonomous Driving at the Crossroads","keynote"),
 ("Alexandre Alahi","EPFL","3 Principles for Building World Models","keynote"),
 ("Sanja Fidler","NVIDIA / University of Toronto","Advancing Autonomous Vehicles with World Models","keynote"),
 ("Alex Kendall","Wayve","Frontier Challenges in Bringing AI to 1B Robots","keynote"),
 ("Vincent Vanhoucke","Waymo","Lessons from Driving 200 Million Fully Autonomous Miles","keynote"),
 ("Shai Shalev-Shwartz","Mobileye","Driving the Long Tail: Efficient Scaling via Automatic Scenario Discovery","keynote"),
 ("Ashok Elluswamy","Tesla","Building Foundational Models for Robotics at Tesla","keynote"),
 ("Raquel Urtasun","Waabi","Reimagining the Physical World with AI","keynote"),
])
add("driving","WDFMEAI","The 1st Workshop on Deployment of Foundation Models for Embodied AI (WDFM-EAI)","https://wdfm-eai.github.io/CVPR26/",1,"Four Seasons 2",[
 ("Peter Stone","Sony AI & University of Texas at Austin","Foundation Models for Robot Navigation, Manipulation, and Planning","keynote"),
 ("Sergey Levine","Physical Intelligence & Berkeley","Robotic Foundation Models","keynote"),
 ("Raquel Urtasun","Waabi & University of Toronto",None,"keynote"),
 ("Alex Kendall","Wayve","Frontier Challenges in Bringing AI to 1B Robots","keynote"),
 ("Dragomir Anguelov","Waymo","Demonstrably Safe AI for Autonomous Driving","keynote"),
 ("Danny Guo","Uber","Uber AV Labs: Where Autonomy Meets Reality","keynote"),
 ("Ashok Elluswamy","Tesla","Building Foundational Models for Robotics at Tesla","keynote"),
 ("Xianming Liu","XPENG","Building the World Model for Autonomous Driving","keynote"),
 ("Ben Snyder","GM","Perceptual, Behavioral, and Outcome Foundation Models for Self-driving","keynote"),
 ("Jan Kautz","NVIDIA","Bringing Humanoid Robots to Life","keynote"),
])
add("driving","Precognition","The Eighth Workshop on Precognition: Seeing through the Future","https://sites.google.com/view/ieeecvf-cvpr2026-precognition",2,"210/212",[
 ("Shivam Gautam","Latitude AI","L3 Is Not L4 Minus One: Perception at Latitude AI","invited"),
 ("Bhiksha Raj","Carnegie Mellon University (LTI)",None,"invited"),
])
add("driving","VOCVALC","9th International Workshop on Visual Odometry (VOCVALC)","https://sites.google.com/view/vocvalc2026/home",2,None,[
 ("Jorge Dias","Khalifa University","NeuroVIO: A Spiking-Hybrid Neuromorphic Computing Framework","invited"),
 ("Lorenzo Torresani","Northeastern University","Where Perception Isn't Enough","invited"),
 ("Junsong Yuan","SUNY at Buffalo","Disentangling Appearance, Geometry, Motion, and Location for Video","invited"),
 ("Jose M. Alvarez","NVIDIA",None,"invited"),
 ("Lantao Liu","Indiana University Bloomington","From Geometry to Semantics: Efficient Autonomous Navigation in the Wild","invited"),
])
add("driving","MEIS","Multi-Agent Embodied Intelligent Systems Meet Agentic-AI era","https://coop-intelligence.github.io/",2,None,[
 ("Xiangbo Gao","Texas A&M University","Opening Keynote","keynote"),
 ("Xiaopeng Li","University of Wisconsin-Madison","Agentic AI for Smart Transportation","keynote"),
 ("Manabu Tsukada","The University of Tokyo","Cooperative Intelligence for Autonomous Driving","keynote"),
 ("Bolei Zhou","UCLA","Scalable Physical AI for Sidewalk Autonomy","keynote"),
 ("Marco Pavone","Stanford University","Physical AI for End-to-End Vehicle Autonomy","keynote"),
 ("Yanjia Huang","Texas A&M University","Web based simulation teleoperation for general manipulation","keynote"),
 ("Angela Dai","Technical University of Munich",None,"keynote"),
 ("Bernadette Bucher","University of Michigan","Bridging the Interaction Gap","keynote"),
 ("Jiachen Li","UC Riverside",None,"keynote"),
])
add("driving","Agents4AD","Third Workshop on Simulation for Autonomous Driving (Agents4AD)","https://agents4ad.github.io/",2,"102/104",[
 ("Marco Pavone","Stanford University / NVIDIA",None,"keynote"),
 ("Cathy Wu","MIT",None,"keynote"),
 ("Hongyang Li","The University of Hong Kong","Simulation at Scale for Production-level Autonomous Driving","invited"),
 ("Dragomir Anguelov","Waymo","The Waymo World Model","invited"),
 ("Siva Manivasagam","Waabi","Building Scalable Closed-Loop Worlds for Safe Autonomous Driving","invited"),
 ("Sanja Fidler","NVIDIA",None,"panel"),
 ("Jose Alvarez","NVIDIA",None,"panel"),
 ("Andrei Bursuc","Valeo",None,"panel"),
])

# ---------------- Computational Imaging ----------------
add("comp-imaging","CCD","Computational Cameras and Displays (CCD)","https://alumni.media.mit.edu/~ayush/CCD/",1,"Mile High 4CD",[
 ("Aydogan Ozcan","UCLA","Programming Light Diffraction for Information Processing and Computational Imaging","keynote"),
 ("Abbie T. Watnik","U.S. Naval Research Lab","Computational Imaging Cameras in the Presence of Laser Interference","keynote"),
 ("Arka Majumdar","University of Washington","Computational Imaging with Meta-Optics Across Length Scales","keynote"),
 ("Gordon Wetzstein","Stanford University","From World Models to World Agents","keynote"),
 ("David B. Lindell","University of Toronto","Foundation Models for Computational Photography","invited"),
 ("Chris Metzler","University of Maryland","Imaging Through Obscurants with Machine Learning","invited"),
 ("Sara Fridovich-Keil","Georgia Tech","When, Why, and How do Diffusion Posterior Samplers Fail?","invited"),
])
add("comp-imaging","UG2Plus","The 8th UG2+ Workshop and Challenge","https://cvpr2026ug2challenge.github.io/",2,"Mile High 4EF",[
 ("Srinivasa Narasimhan","Carnegie Mellon University",None,"keynote"),
 ("Robby T. Tan","National University of Singapore",None,"keynote"),
 ("Matthew O'Toole","Carnegie Mellon University",None,"keynote"),
 ("Felix Heide","Princeton University",None,"keynote"),
 ("Huaijin 'George' Chen","University of Hawaii at Manoa",None,"keynote"),
])
add("comp-imaging","NTIRE","11th New Trends in Image Restoration and Enhancement (NTIRE)","https://www.cvlai.net/ntire/2026/",2,"207",[
 ("Danda Pani Paudel","INSAIT","Relightable 3D Scene Modeling and Understanding Beyond Geometry","invited"),
 ("Sunghyun Cho","POSTECH",None,"invited"),
 ("Marcos V. Conde","University of Wurzburg",None,"invited"),
 ("Ismini Lourentzou","UIUC","From Better Pixels to Better Grounding","invited"),
 ("Yeying Jin","Tencent","Game World Model","invited"),
])

# ---------------- Video: Action & Event Understanding ----------------
add("video","EgoVis","Third Joint Egocentric Vision (EgoVis) Workshop","https://egovis.github.io/cvpr26",1,"704/706",[
 ("Marc Pollefeys","ETH Zurich",None,"keynote"),
 ("Saurabh Gupta","University of Illinois","Video Understanding for Robot Learning","keynote"),
 ("Jawahar C V","IIIT Hyderabad",None,"keynote"),
 ("Lorenzo Torresani","Northeastern University","Where Perception Isn't Enough: Anticipation, Guidance, and Reasoning Over Video","keynote"),
 ("Hazel Doughty","Leiden University","The Devil is in the Details: Towards Fine-Grained Understanding with Limited Supervision","keynote"),
 ("Ziwei Liu","Nanyang Technological University","From Egocentric Experience to Interactive Intelligence","keynote"),
])
add("video","CV4Smalls","Computer Vision with Small Data (CV4Smalls)","https://cv4smalls2026.sites.northeastern.edu/",1,"102/104",[
 ("Vasudev Lal","Oracle","Learning More from Less Multimodal Data","keynote"),
 ("Juan Carlos Niebles","Salesforce AI Research & Stanford University","Agentic Ambient Intelligence: Perception, Reasoning & Action","keynote"),
 ("Jason Corso","Voxel51",None,"panel"),
 ("Jose M. Alvarez","NVIDIA",None,"panel"),
 ("Shuai Zhang","Qualcomm",None,"panel"),
 ("Vimal Bhat","Amazon",None,"panel"),
 ("Sanjeev J. Koppal","Amazon",None,"panel"),
])
add("video","VITA","The 1st Workshop on Vision for Intelligent Task Assistants (VITA)","https://vita-workshop.github.io/cvpr2026/",1,"108",[
 ("David Hayden","Meta","Aria as a Remote-Expert Data Collection Platform","invited"),
 ("Evgeniy Oleinik","Meta","Aria as a Remote-Expert Data Collection Platform (co-presented)","invited"),
 ("Kristen Grauman","University of Texas at Austin","Skill++: Learning to Assess and Improve Physical Skills from Video","invited"),
 ("Ivan Laptev","MBZUAI",None,"invited"),
 ("Gedas Bertasius","UNC Chapel Hill","From Perception to Agency: The Cognitive Stack for Video Task Assistants","invited"),
 ("Marc Pollefeys","ETH Zurich",None,"invited"),
 ("Juan Carlos Niebles","Salesforce AI Research",None,"invited"),
 ("Antonino Furnari","University of Catania","Towards Always-On Wearable AI That Perceives, Understands, and Assists","invited"),
 ("Steven Feiner","Columbia University",None,"invited"),
])
add("video","LOVEU","6th International Workshop on Long-form Video Understanding (LOVEU)","https://sites.google.com/view/loveucvpr26",2,"704/706",[
 ("Yu-xiong Wang","UIUC",None,"invited"),
 ("Manling Li","Northeastern University",None,"invited"),
 ("Yaoyao Liu","UIUC",None,"invited"),
 ("Ruben Villegas","Google DeepMind",None,"invited"),
 ("Xin (Eric) Wang","UCSB and Simular",None,"invited"),
])
add("video","SAUAFG","Second Workshop on Skilled Activity Understanding, Assessment & Feedback Generation (SAUAFG)","https://sauafg-workshop.github.io/",2,"705/707",[
 ("Walterio Mayol-Cuevas","University of Bristol + Amazon","Skill Evolution","keynote"),
 ("Anwesa Choudhuri","United Imaging Intelligence","MedGRPO: Multi-Task RL for Heterogeneous Medical Video Understanding","keynote"),
 ("Guodong Ding","National University of Singapore","From Action Segmentation to Skill Understanding","keynote"),
])

# ---------------- 3D from Multi-View & Sensors ----------------
add("3d","USM3D","Urban Scene Modeling (USM3D)","https://usm3d.github.io",1,"Mile High 3B",[
 ("Matthias Niessner","Technical University of Munich; Synthesia; SpAItial",None,"keynote"),
 ("Florent Lafarge","Inria","Two Decades of 3D Building Reconstruction","keynote"),
 ("Marc Pollefeys","ETH Zurich",None,"keynote"),
 ("Vasileios Balntas","Imperial College London",None,"keynote"),
 ("Angel Xuan Chang","Simon Fraser University",None,"keynote"),
 ("Daniel Barath","ETH Zurich",None,"keynote"),
])
add("3d","ScanNetpp","3rd Workshop on ScanNet++","https://scannetpp.mlsg.cit.tum.de/scannetpp/cvpr2026",1,"710",[
 ("Andrea Tagliasacchi","Simon Fraser University","Explicit Representations for Novel View Synthesis and Generative Modeling","invited"),
 ("David Novotny","Meta AI Research","Building physically-grounded world models","invited"),
 ("Or Litany","NVIDIA Spatial Intelligence Lab / Technion","Seeing by Generating: Novel View Synthesis as a Route to 3D Understanding","invited"),
 ("Peter Hedman","Meta, London","You Can't Wear a World Model: Generating 3D for AR/VR","invited"),
 ("Deva Ramanan","Carnegie Mellon University","Good Old Fashioned 3D Vision vs Pixel Generation","invited"),
])
add("3d","SInT4CH","Spatial Intelligence for Cultural Heritage (SInT4CH)","https://sint4ch.fbk.eu/home",1,"708",[
 ("Qixing Huang","University of Texas at Austin",None,"invited"),
 ("Iro Armeni","Stanford University",None,"invited"),
 ("Hadar Averbuch-Elor","Cornell University & Cornell Tech",None,"invited"),
 ("Deblina Bhattacharjee","University of Bath, UK",None,"invited"),
])
add("3d","ThreeDMV","Third Workshop for Learning 3D with Multi-View Supervision (3DMV)","https://3dmv.org/2026/",2,"703",[
 ("Matthias Niessner","TU Munich","3D Scene Reconstruction","keynote"),
 ("Ziwei Liu","Nanyang Technological University","Multi-view Generative Diffusion Models","keynote"),
 ("Andrea Vedaldi","University of Oxford","Building a 3D Foundation for Spatial AI","keynote"),
])
add("3d","SPAR3D","SPAR-3D: Security, Privacy, and Adversarial Robustness in 3D Generative Vision","https://www.spar3d.org/",2,"Mile High 3A",[
 ("Avideh Zakhor","UC Berkeley",None,"keynote"),
 ("Sangpil Kim","Korea University",None,"keynote"),
 ("Duen Horng (Polo) Chau","Georgia Tech",None,"keynote"),
 ("John Collomosse","Adobe & University of Surrey",None,"keynote"),
])
add("3d","FourDVision","2nd Workshop on 4D Vision: Modeling the Dynamic World","https://4dvisionworkshop.github.io/",2,"506",[
 ("Georgios Pavlakos","UT Austin",None,"invited"),
 ("Jiajun Wu","Stanford University",None,"invited"),
 ("Dima Damen","University of Bristol / Google DeepMind",None,"invited"),
 ("Srinath Sridhar","Brown University",None,"invited"),
 ("Noah Snavely","Cornell Tech / Google DeepMind",None,"invited"),
 ("Chaoyang Wang","Snap",None,"invited"),
])
add("3d","ImageMatching","Eighth Workshop on Image Matching: Local Features and Beyond","https://image-matching-workshop.github.io/",2,"504",[
 ("Paul-Edouard Sarlin","Google",None,"invited"),
 ("Nikhil Keetha","CMU / Meta",None,"invited"),
 ("Jianyuan Wang","Oxford / Meta",None,"invited"),
])

# ---------------- Vision Applications & Systems ----------------
add("applications","AI4RWC","AI4RWC: 2nd International Workshop on Vision Intelligence for Real-world Challenges","https://sites.google.com/view/ai4rwc2026",1,"507",[
 ("Andre Altmann","University College London","AI for Solving Real-World Challenges in Brain Imaging","keynote"),
 ("Alex Zhou","Linkerbot",None,"invited"),
 ("Mandy Ma","Linkerbot","Linkerbot: From Hand to Data to Action","invited"),
])
add("applications","CV4AEC","Computer Vision for the Built World (CV4AEC)","https://cv4aec.github.io/",1,"109",[
 ("Semiha Ergan","NYU",None,"keynote"),
 ("Jia Deng","Princeton",None,"keynote"),
 ("Debra Laefer","NYU",None,"keynote"),
 ("Huaizu Jiang","Northeastern",None,"keynote"),
])
add("applications","MetaFood","The 3rd MetaFood Workshop (MTF)","https://sites.google.com/view/cvpr-metafood-2026",1,"709",[
 ("Dima Damen","University of Bristol",None,"keynote"),
 ("Tapomayukh Bhattacharjee","Cornell University",None,"keynote"),
])
add("applications","AgricultureVision","The 7th Agriculture-Vision Workshop","https://www.agriculture-vision.com",1,"2A",[
 ("Jason Corso","University of Michigan",None,"invited"),
 ("Soumik Sarkar","Iowa State University",None,"invited"),
 ("Shenlong Wang","UIUC",None,"invited"),
 ("Girish Chowdhary","UIUC",None,"invited"),
 ("Gary Bradski","OpenCV",None,"invited"),
])
add("applications","OmniCV","6th Omnidirectional Computer Vision Workshop (OmniCV)","https://sites.google.com/view/omnicv2026",2,"711",[
 ("Junho Kim","Seoul National University",None,"keynote"),
 ("Huajian Huang","HKUST",None,"keynote"),
 ("Mike Lambeta","Meta (FAIR Robotics)",None,"keynote"),
 ("Xin Lin","UC San Diego",None,"keynote"),
])
add("applications","CVsports","12th IEEE International Workshop on Computer Vision in Sports (CVsports)","https://vap.aau.dk/cvsports/",None,None,[
 ("Maaike Van Roy","KU Leuven","Analyzing Soccer Actions and Tactics by Learning and Reasoning","invited"),
 ("Atom Scott","Playbox Inc.","When Sports CV Leaves the Lab","invited"),
 ("Christina Chase","MIT Sports Lab","From Tracking to Understanding: The Next Decade of CV in Sports","invited"),
 ("Johsan Billingham","FIFA","FIFA Research - Case Studies and Research Highlights","invited"),
])
add("applications","AI4Space","Artificial Intelligence for Space (AI4Space)","https://ai4space.space/",None,None,[
 ("David Rijlaarsdam","Ubotica Technologies",None,"keynote"),
 ("Marco Pavone","Stanford University / NVIDIA",None,"keynote"),
 ("Ethan Rublee","Space-ng",None,"keynote"),
 ("Yandong Liu","STAR.VISION",None,"panel"),
 ("Manos Koumandakis","Infinite Orbits",None,"panel"),
])

# ---------------- Vision for Societal Good ----------------
add("societal","APAI","Authenticity & Provenance in the age of Generative AI (APAI)","https://sites.google.com/stanford.edu/apai-cvpr2026/",1,"103",[
 ("Christoph Bregler","Google DeepMind",None,"invited"),
 ("Jill Crisman","Digital Safety Research Institute",None,"invited"),
 ("Pierre Fernandez","FAIR (Meta)",None,"invited"),
 ("Shirin Anlen","WITNESS",None,"invited"),
])
add("societal","CV4Animals","6th Workshop on CV4Animals: Computer Vision for Animal Behavior","https://www.cv4animals.com",2,"108",[
 ("Liang An","Nanjing University / Tsinghua University",None,"invited"),
 ("Federico Rossano","University of California, San Diego",None,"invited"),
 ("Orit Peleg","University of Colorado Boulder / Santa Fe Institute",None,"invited"),
])
add("societal","MisDet","From Perception to Persuasion: Misinformation Detection in Society","https://eecs.uq.edu.au/CVPR2026",None,None,[
 ("Mohan S. Kankanhalli","National University of Singapore","Rethinking Misinformation Defense Through the Lens of Human Behaviour","keynote"),
 ("Gianluca Demartini","The University of Queensland","How Bias in LLMs can Influence Human Decisions","keynote"),
 ("Vimala Balakrishnan","Universiti Malaya","The Psychology of Digital Deception in the Age of AI","keynote"),
])
add("societal","CV4Edu","Computer Vision x Education (CV4Edu)","https://cv4edu.github.io",2,"113",[
 ("Mohit Bansal","UNC Chapel Hill","Understanding Student Engagement & Teacher Facilitation via Multimodal Video Reasoning","keynote"),
 ("Scott Acton","University of Virginia","Advancing Instruction through Computer Vision","keynote"),
 ("Marcelo Worsley","Northwestern University",None,"keynote"),
 ("Jacob Whitehill","Worcester Polytechnic Institute",None,"keynote"),
 ("Gautam Biswas","Vanderbilt University",None,"panel"),
 ("Nikhil Krishnaswamy","Colorado State University",None,"panel"),
 ("Nathaniel Blanchard","Colorado State University",None,"panel"),
 ("Ekta Sood","University of Colorado Boulder",None,"panel"),
 ("Joyce Horn Fonteles","Vanderbilt University",None,"panel"),
 ("Mariah Bradford","Colorado State University",None,"panel"),
])

# ---------------- World Models ----------------
add("world-models","E2E3D","End-to-End 3D Learning (E2E3D)","https://e2e3d.github.io/",1,"501",[
 ("Luca Carlone","MIT",None,"keynote"),
 ("Jiajun Wu","Stanford University",None,"keynote"),
 ("Georgios Pavlakos","UT Austin",None,"keynote"),
 ("Paul-Edouard Sarlin","Google",None,"keynote"),
 ("Marco Pavone","Stanford / NVIDIA",None,"keynote"),
])
add("world-models","GeoFreeNVS","Geometry-Free Novel View Synthesis and Controllable Video Models","https://geofreenvs.github.io/",2,"607",[
 ("Peter Kontschieder","Meta",None,"invited"),
 ("Katja Schwarz","World Labs",None,"invited"),
 ("Yilun Du","Harvard",None,"invited"),
 ("Ning Yu","Netflix",None,"invited"),
 ("Vincent Sitzmann","MIT",None,"invited"),
 ("Aleksander Holynski","Google DeepMind",None,"invited"),
 ("Gordon Wetzstein","Stanford",None,"invited"),
 ("Jiajun Wu","Stanford",None,"invited"),
])
add("world-models","4DWorldModels","4D World Models: Bridging Generation and Reconstruction","https://ivl.cs.brown.edu/4dworldmodels/",2,"203",[
 ("Qianqian Wang","Harvard University",None,"invited"),
 ("Sara Fridovich-Keil","Georgia Tech",None,"invited"),
 ("Youngjoong Kwon","Emory University",None,"invited"),
 ("Peter Kontschieder","Meta Reality Labs",None,"invited"),
 ("Jiahui Lei","UC Berkeley",None,"invited"),
 ("Matthias Niessner","TU Munich",None,"invited"),
])

# ---------------- Multimodal Learning ----------------
add("multimodal","A2AMML","Workshop on Any-to-any Multimodal Learning (A2A-MML)","https://any2any-mllm.github.io/workshop-cvpr26/",2,"502",[
 ("Zhedong Zheng","University of Macau","When AI Thinks Like Humans: Cognitive Biases and Uncertainty Awareness","keynote"),
 ("Saining Xie","NYU",None,"keynote"),
 ("Georgia Gkioxari","Caltech","Beyond Image and Language: Building 3D Perception Systems","keynote"),
 ("Mohit Bansal","UNC Chapel Hill","Multimodal Unification, Communication, and Composable Generalization","keynote"),
 ("Yossi Gandelsman","TTIC","A neuro-analysis of vision and language models","keynote"),
 ("Manling Li","Northwestern","Any-View to Any-View: Learning Spatial Intelligence in Multimodal Models","keynote"),
 ("Paul Liang","MIT","Expanding AI's Senses: Touch, Smell, and Beyond","keynote"),
])
add("multimodal","MULA","9th Multimodal Learning and Applications Workshop (MULA)","https://mula-workshop.github.io/",2,"111",[
 ("Yuki Asano","University of Technology Nuremberg","(Some) Innovations in Vision Encoding","keynote"),
 ("Georgia Gkioxari","Caltech / Meta AI","From Categories to Concepts: Expanding What Vision Language Models Can See","keynote"),
 ("Andrei Bursuc","valeo.ai","Multimodal Large Language Models: Can we make them reliable?","keynote"),
 ("Hedvig Kjellstrom","KTH Royal Institute of Technology","Two Perspectives on Multimodal Estimation and Synthesis","keynote"),
 ("Ranjay Krishna","University of Washington","One Model Enabling Robotics, Computer Use and Motion Modeling","keynote"),
 ("Lorenzo Baraldi","University of Modena and Reggio Emilia","From Retrieval to Reflection to Reasoning","keynote"),
])
add("multimodal","SightAndSound","Sight and Sound","https://sightsound.org/",2,"Mile High 1CD",[
 ("Sophia Koepke",None,None,"invited"),
 ("Dinesh Manocha","University of Maryland",None,"invited"),
 ("Eli Shlizerman","University of Washington",None,"invited"),
 ("Ruohan Gao","Meta / University of Maryland",None,"invited"),
 ("Yake Wei",None,None,"invited"),
])

# ---------------- Safety / Ethics ----------------
add("safety","MUV","Machine Unlearning for Vision (MUV)","https://machine-unlearning-for-vision.github.io",1,"Mile High 1AB",[
 ("Sijia Liu","Michigan State University","Forgetting Unwanted Knowledge in Foundation Models Without Breaking Them","invited"),
 ("Rohit Gandikota","Northeastern University","Unlearning Is Not The Goal, It's Just the Beginning","invited"),
 ("Maximilian Dreyer","Fraunhofer HHI","From Explanation to Unlearning","invited"),
 ("Raymond A. Yeh","Purdue University","Beyond Post-Hoc Unlearning: Immunization and Semi-parametric Design","invited"),
 ("Tsui-Wei (Lily) Weng","UC San Diego","Building Controllable AI with Interpretable Representations","invited"),
])
add("safety","AIMS","The 3rd Workshop on New Trends in AI-Generated Media and Security (AIMS)","https://sites.google.com/view/aims2026",2,"102/104",[
 ("Kevin W. Bowyer","University of Notre Dame","Monozygotic Twins and Face Recognition","keynote"),
 ("Liang Zheng","Australian National University","End-to-end representation learning in generative models","keynote"),
 ("Efim Boieru","Incode Technologies","Deepfake Detection in Production","keynote"),
])
add("safety","TRUEV","Trustworthy, Robust, Uncertainty-Aware, and Explainable Visual Intelligence (TRUE-V)","https://trustworthy-ai-workshop.github.io/cvpr2026-TRUE-V/",2,"705/707",[
 ("Sharon Li","UW-Madison",None,"keynote"),
 ("Somayeh Sojoudi","UC Berkeley","Reliability of Large Language Models: Failures, Robustness, and Interpretability","keynote"),
 ("Furong Huang","University of Maryland",None,"keynote"),
 ("Marina Gavrilova","University of Calgary","Fair Play: Ensuring Trustworthiness and Fair AI Predictions","keynote"),
 ("Emma Pierson","UC Berkeley","Sparse Autoencoders for Hypothesis Generations","keynote"),
 ("Alexandre Alahi","EPFL",None,"keynote"),
])

# ---------------- Scene Analysis & Understanding ----------------
add("scene","OpenSUN3D","OpenSUN3D: 6th Workshop on Open-World 3D Scene Understanding","https://opensun3d.github.io/",1,"705/707",[
 ("Vasileios Balntas","Reality Labs Research",None,"keynote"),
 ("Djamila Aouada","University of Luxembourg",None,"keynote"),
 ("Andrea Tagliasacchi","Simon Fraser University",None,"keynote"),
 ("Chelsea Finn","Stanford University",None,"keynote"),
 ("Aleksander Holynski","Google DeepMind",None,"keynote"),
])
add("scene","SceneUnderstanding3D","6th Workshop on 3D Scene Understanding for Vision, Graphics, and Robotics","https://scene-understanding.com/",2,"610/612",[
 ("Andrew Davison","Imperial College London",None,"invited"),
 ("Gerard Pons-Moll","University of Tubingen",None,"invited"),
 ("Songyou Peng","Google DeepMind",None,"invited"),
 ("Andrea Vedaldi","University of Oxford",None,"invited"),
 ("Ziwei Liu","Nanyang Technological University",None,"invited"),
 ("Lingjie Liu","University of Pennsylvania",None,"invited"),
])
add("scene","PVUW","Pixel-level Video Understanding in the Wild Challenge (PVUW)","https://pvuw.github.io/",2,"502",[
 ("Siyuan Li","ETH Zurich",None,"invited"),
 ("Alexander Schwing","University of Illinois Urbana-Champaign",None,"invited"),
 ("Amir Zamir","EPFL",None,"invited"),
])

# ---------------- Adversarial Attack & Defense ----------------
add("adversarial","SAFE","Synthetic & Adversarial ForEnsics (SAFE)","https://www.safeworkshop.org/cvpr-2026/",1,"107",[
 ("Alina Oprea","Northeastern University","The Way Forward: Towards Trustworthy AI Systems","keynote"),
 ("Zhiyuan Yu","Texas A&M University","Securing Data Agency in the Synthetic Era","keynote"),
 ("Xiaoming Liu","UNC Chapel Hill","On the Detection, Localization and Reverse Engineering of AI-Generated Visual Content","keynote"),
 ("David Harwath","The University of Texas at Austin",None,"keynote"),
])
add("adversarial","AdvML","The 6th Workshop of Adversarial Machine Learning on Computer Vision (AdvML)","https://cvpr26-advml.github.io/",2,"708",[
 ("Bo Li","University of Illinois at Urbana-Champaign",None,"invited"),
 ("Chaowei Xiao","Johns Hopkins University",None,"invited"),
 ("Aditi Raghunathan","Carnegie Mellon University",None,"invited"),
 ("Florian Tramer","ETH Zurich",None,"invited"),
 ("Nouha Dziri","Cohere Labs",None,"invited"),
 ("Jingwei Yi","BAAI",None,"invited"),
 ("Ziwei Liu","Nanyang Technological University",None,"invited"),
])

# ---------------- Open World Learning ----------------
add("open-world","OpenWorldVision","Open-World Vision","https://vplow.github.io/vplow_6th.html",2,"712",[
 ("Shu Kong","University of Macau & OIST","Visual Perception via Learning in an Open World","invited"),
 ("Walter J. Scheirer","University of Notre Dame",None,"invited"),
 ("Sathyanarayanan Aakur","Auburn University","Understanding Open-World Human Behavior through Active Event Perception","invited"),
 ("Marc Pollefeys","ETH Zurich / Microsoft",None,"invited"),
 ("Jiajun Wu","Stanford University",None,"invited"),
 ("Boqing Gong","Boston University",None,"invited"),
 ("Neehar Peri","Carnegie Mellon University","Insights and Lessons in FSOD","invited"),
])
add("open-world","ADFM","The Third Workshop on Anomaly Detection with Foundation Models","https://adfmw.github.io/cvpr26/",2,"712",[
 ("Danijel Skocaj","University of Ljubljana","Towards a Universal Foundation Model for Visual Anomaly Detection","keynote"),
 ("Sanjay Chawla","Qatar Computing Research Institute","OOD Detection and Generalization: Challenges and Opportunities","keynote"),
])
add("open-world","VAND","Visual Anomaly and Novelty Detection - 4th Edition (VAND)","https://sites.google.com/view/vand4-cvpr2026",2,"601",[
 ("Walter Scheirer","University of Notre Dame","Open Issues in Open World Learning","invited"),
 ("Bodo Rosenhahn","Leibniz University Hannover","Anomaly Detection using Normalizing Flows","invited"),
 ("Sebastian Hofer","Amazon","Visual Defect Detection in Retail Logistics: The Kaputt Dataset","invited"),
 ("David Zimmerer","DKFZ","Measure What Matters: Radiological Anomaly Localisation","invited"),
])

# ===================== assemble =====================
workshops = {}
talks = []
speaker_index = {}
tid = 0
for w in W:
    spk = [{"name": n, "affil": a, "title": t, "role": r} for (n, a, t, r) in w["speakers"]]
    workshops[w["key"]] = {
        "name": w["name"], "url": w["url"], "category": w["category"],
        "day": w["day"], "room": w["room"], "note": w["note"], "speakers": spk,
    }
    for (n, a, t, r) in w["speakers"]:
        talks.append({
            "id": "k%d" % tid, "ws": w["key"], "category": w["category"],
            "day": w["day"], "room": w["room"], "who": n, "affil": a,
            "title": t, "role": r,
        })
        speaker_index.setdefault(n, []).append({"ws": w["key"], "role": r, "title": t})
        tid += 1

# multi-workshop speakers (sorted by appearance count, desc)
multi = {n: v for n, v in speaker_index.items() if len(v) > 1}

out = {
    "meta": {
        "conference": "CVPR 2026",
        "location": "Denver, CO",
        "dates": "June 2026 (workshops June 3-4; day 1 = Wed Jun 3, day 2 = Thu Jun 4)",
        "generated": "2026-06-03",
        "source": "Official per-workshop pages, scraped June 2026.",
        "note": "Exhaustive catalog of every CVPR 2026 workshop and its invited/keynote/panel speakers. Times are not included (most per-talk times are unpublished); for a curated, time-gridded subset see cvpr2026-data.json.",
        "counts": {
            "workshops": len(workshops),
            "speaker_slots": len(talks),
            "unique_speakers": len(speaker_index),
            "multi_workshop_speakers": len(multi),
        },
    },
    "categories": {k: {"label": v[0], "c": v[1]} for k, v in CATEGORIES.items()},
    "workshops": workshops,
    "talks": talks,
    "speakerIndex": {n: v for n, v in sorted(speaker_index.items(), key=lambda kv: (-len(kv[1]), kv[0]))},
}

path = os.path.join(os.path.dirname(__file__), "..", "public", "cvpr2026-all.json")
with open(path, "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

print("Wrote", os.path.abspath(path))
print("workshops:", len(workshops))
print("speaker slots:", len(talks))
print("unique speakers:", len(speaker_index))
print("multi-workshop speakers:", len(multi))
top = sorted(multi.items(), key=lambda kv: -len(kv[1]))[:15]
for n, v in top:
    print("  %2d  %s" % (len(v), n))

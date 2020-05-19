db.createUser(
    {
        user: "mongo",
        pwd: "secret",
        roles: [
            {
                role: "readWrite",
                db: "mlDatabase"
            }
        ]
    }
)
db.articles.insertMany(
    [
        {
            "authors": [
                "S. Popov",
                "S. Morozov",
                "A. Babenko"
            ],
            "name": "Neural Oblivious Decision Ensembles for Deep Learning on Tabular Data",
            "meta": "2020, ICLR",
            "imageUrl": "https://avatars.mds.yandex.net/get-research/1925584/2a000001703cf46c3c81d67db1e713b1ed3f/orig",
            "articleUrl": "https://research.yandex.com/publications/241",
            "source": "yandex",
            "date": "14 Feb 2020",
            "abstract": "Nowadays, deep neural networks (DNNs) have become the main instrument for machine learning tasks within a wide range of domains, including vision, NLP, and speech. Meanwhile, in an important case of heterogenous tabular data, the advantage of DNNs over shallow counterparts remains questionable. In particular, there is no sufficient evidence that deep learning machinery allows constructing methods that outperform gradient boosting decision trees (GBDT), which are often the top choice for tabular problems. In this paper, we introduce Neural Oblivious Decision Ensembles (NODE), a new deep learning architecture, designed to work with any tabular data. In a nutshell, the proposed NODE architecture generalizes ensembles of oblivious decision trees, but benefits from both end-to-end gradient-based optimization and the power of multi-layer hierarchical representation learning. With an extensive experimental comparison to the leading GBDT packages on a large number of tabular datasets, we demonstrate the advantage of the proposed NODE architecture, which outperforms the competitors on most of the tasks. We open-source the PyTorch implementation of NODE and believe that it will become a universal framework for machine learning on tabular data.",
            "researchAreas": [
                "Machine Learning"
            ]
        },
        {
            "researchAreas": ["COMPUTER VISION"],
            "name": "Single-Network Whole-Body Pose Estimation | Facebook AI Research",
            "authors": [
                "Gines Hidalgo",
                "Yaadhav Raaj",
                "Haroon Idrees",
                "Donglai Xiang",
                "Hanbyul Joo",
                "Tomas Simon",
                "Yaser Sheikh"
            ],
            "articleUrl": "https://ai.facebook.com/research/publications/single-network-whole-body-pose-estimation/",
            "abstract": "We present the first single-network approach for 2D whole-body pose estimation, which entails simultaneous localization of body, face, hands, and feet keypoints. Due to the bottom-up formulation, our method maintains constant real-time performance regardless of the number of people in the image. The network is trained in a single stage using multi-task learning, through an improved architecture which can handle scale differences between body/foot and face/hand keypoints. Our approach considerably improves upon OpenPose [9], the only work so far capable of whole-body pose estimation, both in terms of speed and global accuracy. Unlike [9], our method does not need to run an additional network for each hand and face candidate, making it substantially faster for multi-person scenarios. This work directly results in a reduction of computational complexity for applications that require 2D whole-body information (e.g., VR/AR, re-targeting). In addition, it yields higher accuracy, especially for occluded, blurry, and low resolution faces and hands. For code, trained models, and validation benchmarks, visit our project page."
        }
    ]
)
# 📊 Datasets

This directory contains raw and processed datasets for the fake news detection system.

## Datasets Used

### English
| Dataset | Description | Size | Source |
|---------|-------------|------|--------|
| **ISOT** | Real & fake news articles (2016-2017) | ~44K articles | [ISOT Dataset](https://www.uvic.ca/ecs/ece/isot/datasets/fake-news/index.php) |
| **AVeriTeC** | Fact verification with evidence | ~4.5K claims | [AVeriTeC](https://fever.ai/dataset/averitec.html) |
| **X-FACT** | Multilingual fact-check dataset | ~31K claims, 25 languages | [X-FACT](https://github.com/utahnlp/x-fact) |

### Hindi
| Dataset | Description | Size | Source |
|---------|-------------|------|--------|
| **Hindi Fake News** | Hindi news articles labeled real/fake | ~3.5K articles | [GitHub](https://github.com/sumanthvrao/Fake-News-Detection-Hindi) |
| **IndicNLP News** | Indian language news corpus | Various | [AI4Bharat](https://indicnlp.ai4bharat.org/) |

## Directory Structure

```
data/
├── raw/              # Original downloaded datasets (not committed to git)
│   └── .gitkeep
├── processed/        # Cleaned, tokenized, split datasets (not committed)
│   └── .gitkeep
└── README.md         # This file
```

## Download Instructions

1. Download datasets from the links above
2. Place raw files in `data/raw/`
3. Run the data preparation notebook: `notebooks/01_data_preparation.ipynb`
4. Processed data will be saved to `data/processed/`

## License Notes

- **ISOT**: Academic use only — check original license
- **AVeriTeC**: CC BY-SA 4.0
- **X-FACT**: Apache 2.0
- Hindi datasets: Check individual repository licenses

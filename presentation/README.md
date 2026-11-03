# Presentation

Git cannot merge `.pptx` files, so each part has a separate deck.

- template.pptx: shared editable 16:9 theme. Keep its font and palette in both decks.
- design_detection.pptx: eight slides for final positions 1, 2, 3, 4 (H1 and H3 half), 6, 10, 11 (detection half) and 12.
- data_quality.pptx: six slides for final positions 4 (H2 half), 5, 7, 8, 9 and 11 (ratings and data half).
- final.pptx: create after both member decks and shared slides are reviewed. No combined final deck is claimed yet.

| Final slide | Topic | Owner | Member-deck position |
|---|---|---|---|
| 1 | Title and research question | Debshree | design_detection 1 |
| 2 | Motivation | Debshree | design_detection 2 |
| 3 | Design and passages | Debshree | design_detection 3 |
| 4 | Hypotheses and power | Both | design_detection 4 + data_quality 1 |
| 5 | Participant flow | Kuba | data_quality 2 |
| 6 | H1 group comparison | Debshree | design_detection 5 |
| 7 | H2 quality | Kuba | data_quality 3 |
| 8 | Assumptions and items | Kuba | data_quality 4 |
| 9 | Exploratory regression | Kuba | data_quality 5 |
| 10 | H3 and confidence | Debshree | design_detection 6 |
| 11 | Limitations | Both | design_detection 7 + data_quality 6 |
| 12 | Conclusion and recommendations | Both | design_detection 8 |

Each deck's visible numbers refer to the final sequence. Merge slide 4's halves and the limitations points after joint review. Say that the written plan labelled the group comparison exploratory, and keep the fixed-order limitation visible; if the course time limit requires cuts, preserve it. Charts are native editable objects, speaker notes cite their sources, and every number comes from results/quality/.

## Rebuild

Run `make slides`, which uses python-pptx and the shared template and needs no raw participant data. Review every rendered slide after content changes. `make slides` rebuilds both decks, so commit only the deck you changed. To change a slide, edit its builder: scripts/quality/build_slides.py or scripts/detection/build_design_slides.py.

Debshree’s reviewed design deck emphasizes correct-in-coding = Passage 1, the retrospective exclusions/priority, and power at .05/3. The final conclusion slide is a joint-discussion draft. The generator normalizes chart-axis IDs for portable import and keeps charts editable. To preserve the other member’s binary deck while running the shared target, build in an isolated copy and copy back only the assigned deck; do not commit a regenerated data_quality.pptx from this task.

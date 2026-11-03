# Presentation

Git cannot merge `.pptx` files, so each part has a separate deck.

- template.pptx: shared editable 16:9 theme. Keep its font and palette in both decks.
- design_detection.pptx: seven slides for final positions 1, 2, 3, 4 (H1 half), 6, 10 (detection half) and 11.
- data_quality.pptx: six slides for final positions 4 (H2 half), 5, 7, 8, 9 and 10 (ratings and data half).
- final.pptx: the combined 11-slide draft, built from both member decks by scripts/build_final_deck.py. It merges slides 4 and 11, labels each slide's presenter in the speaker notes, and awaits review by both members.

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
| 10 | Limitations | Both | design_detection 6 + data_quality 6 |
| 11 | Conclusion and recommendations | Both | design_detection 7 |

Each deck's visible numbers refer to the final sequence. `make slides` merges slide 4's halves and the limitations points in final.pptx. Say that the written plan labelled the group comparison exploratory, and keep the fixed-order limitation visible; if the course time limit requires cuts, preserve it. Charts are native editable objects, speaker notes cite their sources, and every number comes from results/quality/.

## Rebuild

Run `make slides`, which uses python-pptx and the shared template and needs no raw participant data. Review every rendered slide after content changes. `make slides` rebuilds all three decks; rebuild and commit final.pptx with any deck you change. To change a slide, edit its builder: scripts/quality/build_slides.py, scripts/detection/build_design_slides.py, or scripts/build_final_deck.py for slides 4 and 10. Hand edits to a deck are overwritten.

Debshree’s reviewed design deck emphasizes correct-in-coding = Passage 2, the retrospective exclusions/priority, and power at .05. The final conclusion slide is a joint-discussion draft. The generator normalizes chart-axis IDs for portable import and keeps charts editable. To preserve the other member’s binary deck while running the shared target, build in an isolated copy and copy back only the assigned deck; do not commit a regenerated data_quality.pptx from this task.

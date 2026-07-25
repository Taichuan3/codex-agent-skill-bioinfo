# Drug Screening and ADMET Decision Matrix

| Decision need | Evidence or method | Required record | Boundary |
|---|---|---|---|
| Target evidence | genetics/QTL, perturbation, expression/context, literature, tractability, safety liabilities | source/version, study design, tissue/context, effect direction, uncertainty | association is not causality |
| Measured bioactivity | ChEMBL, BindingDB, PubChem BioAssay or curated primary sources | compound identity, assay/construct/species, endpoint, relation, value, units, confidence | assay values are not automatically comparable |
| Virtual-screen campaign | chemical library, physicochemical/reactivity filters, docking summary, orthogonal scores | raw/standardized mapping, filter order, attrition, score definition, controls | rank is protocol-specific and exploratory |
| QSAR/property model | descriptor, classical ML, graph/deep-learning or curated predictor | endpoint, training provenance, split, baseline, domain, calibration/uncertainty | prediction is not measurement |
| ADMET triage | absorption, distribution, metabolism, excretion and toxicity endpoints | endpoint-specific units/classes, source/model version, domain, alert, uncertainty | no single “ADMET score” proves safety |
| Repurposing | target/pathway/omics reversal, prior bioactivity, clinical/regulatory context | indication/context, evidence type, date, mismatch and next validation | candidate background is not efficacy |
| Molecule generation | scaffold decoration or generative model followed by validity/deduplication checks | generation settings, validity, uniqueness, novelty policy, synthesis/risk checks | generated structure is not a viable drug |

## Campaign sequence

1. Define the decision, target/context, compound universe, endpoints and validation budget.
2. Preserve raw identifiers and structures; standardize into a versioned analysis table with an explicit mapping.
3. Establish simple baselines and controls before complex ranking or generation.
4. Run a bounded pilot; report input count, standardization/invalid/duplicate/filter attrition, prediction coverage and failures.
5. Keep measured, curated, inferred, text-mined, docking-derived and model-predicted evidence in separate columns.
6. Rank by declared dimensions and rules; test sensitivity to weights, missing-data policy and conflicting evidence.
7. Apply stop/pivot criteria and nominate the smallest orthogonal experiment that can change the decision.

## Candidate table minimum fields

`candidate_id, raw_id, standardized_structure_id, target_or_context, evidence_layer, endpoint_or_metric, relation, value, units, source, version_or_date, model_or_assay, applicability_or_confidence, uncertainty, qc_status, caveat, next_validation`

Do not average incompatible endpoints or tool scores merely to produce one rank. Keep missing, not-applicable, failed and not-assessed states distinct.

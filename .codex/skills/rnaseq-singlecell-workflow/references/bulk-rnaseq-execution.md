# Bulk RNA-seq Execution

## Intake contract

Record:

- FASTQ/BAM/count matrix provenance, checksums or manifest pointers;
- sample ID, biological replicate, condition, batch, paired/blocked structure and exclusions;
- organism, genome build, transcript annotation release, read layout and strandedness;
- primary estimand and exact contrasts.

Do not proceed to differential testing when sample identity, replicate structure, design rank or count provenance is unresolved.

## FASTQ or BAM to abundance

1. Inspect a representative input and sample-sheet row before a full run.
2. Verify read quality, adapter/content signals, read pairing and expected sample count.
3. Choose alignment plus feature counting or transcript-aware quantification according to the estimand.
4. Record reference FASTA, annotation, index build, tool versions, parameters and random seeds where relevant.
5. Review mapping/pseudoalignment, assignment, duplication/complexity, strandedness and contamination signals across samples.
6. Preserve logs and machine-readable QC; aggregation tools summarize upstream metrics but do not define pass/fail by themselves.

## Count matrix to differential expression

1. Confirm integer/raw-count expectations and gene identifier namespace.
2. Compare roster, library size, detected features, zero structure, sample correlation/PCA and known identity covariates.
3. Define independent filtering and low-expression rules before inspecting favored genes.
4. Fit a full-rank, sample-level design with explicit contrasts; preserve model formula, reference levels and multiple-testing method.
5. Use transformed values for QC/visualization, not as a silent substitute for count-aware testing.
6. Report effect size, uncertainty, adjusted significance, base expression and the tested population; do not rank on p-value alone.

## Transcript usage and splicing

- Match the method to transcript-, event- or junction-level evidence.
- Record annotation dependence, read support, minimum coverage, event definition and ambiguity handling.
- Treat short-read isoform attribution cautiously; distinguish differential usage from total-gene abundance.
- Require orthogonal or targeted validation before strong isoform-function claims.

## Minimum outputs

- validated sample/design table;
- config/command and software/reference provenance;
- per-sample and cross-sample QC with exclusion decisions;
- analysis-ready abundance object and complete result tables;
- source data for reported figures and a concise limitations record.

Stop and report when replicate count, confounding, sample swaps, pervasive low quality or design singularity prevents the intended inference.

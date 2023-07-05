from mmengine.config import read_base

with read_base():
    from ..mmlu.mmlu_gen_a568f1 import mmlu_datasets
    from ..ceval.ceval_gen_ee2cb0 import ceval_datasets
    from ..agieval.agieval_gen_dc7dae import agieval_datasets
    from ..GaokaoBench.GaokaoBench_gen_aed980 import GaokaoBench_datasets
    from ..bbh.bbh_gen_58abc3 import bbh_datasets
    from ..humaneval.humaneval_gen_d428f1 import humaneval_datasets
    from ..mbpp.mbpp_gen_4104e4 import mbpp_datasets
    from ..CLUE_C3.CLUE_C3_gen_9e3de9 import C3_datasets
    from ..CLUE_CMRC.CLUE_CMRC_gen_72a8d5 import CMRC_datasets
    from ..CLUE_DRCD.CLUE_DRCD_gen_03b96b import DRCD_datasets
    from ..CLUE_afqmc.CLUE_afqmc_gen_db509b import afqmc_datasets
    from ..CLUE_cmnli.CLUE_cmnli_gen_316313 import cmnli_datasets
    from ..CLUE_ocnli.CLUE_ocnli_gen_7c44b0 import ocnli_datasets
    from ..FewCLUE_bustm.FewCLUE_bustm_gen_305431 import bustm_datasets
    from ..FewCLUE_chid.FewCLUE_chid_gen_686c63 import chid_datasets
    from ..FewCLUE_cluewsc.FewCLUE_cluewsc_gen_276956 import cluewsc_datasets
    from ..FewCLUE_csl.FewCLUE_csl_gen_1b0c02 import csl_datasets
    from ..FewCLUE_eprstmt.FewCLUE_eprstmt_gen_d6d06d import eprstmt_datasets
    from ..FewCLUE_ocnli_fc.FewCLUE_ocnli_fc_gen_bef37f import ocnli_fc_datasets
    from ..FewCLUE_tnews.FewCLUE_tnews_gen_8d59ba import tnews_datasets
    from ..lcsts.lcsts_gen_427fde import lcsts_datasets
    from ..lambada.lambada_gen_7ffe3d import lambada_datasets
    from ..storycloze.storycloze_gen_c5a230 import storycloze_datasets
    from ..SuperGLUE_AX_b.SuperGLUE_AX_b_gen_477186 import AX_b_datasets
    from ..SuperGLUE_AX_g.SuperGLUE_AX_g_gen_7a5dee import AX_g_datasets
    from ..SuperGLUE_BoolQ.SuperGLUE_BoolQ_gen_8525d1 import BoolQ_datasets
    from ..SuperGLUE_CB.SuperGLUE_CB_gen_bb97e1 import CB_datasets
    from ..SuperGLUE_COPA.SuperGLUE_COPA_gen_6d5e67 import COPA_datasets
    from ..SuperGLUE_MultiRC.SuperGLUE_MultiRC_gen_26c9dc import MultiRC_datasets
    from ..SuperGLUE_RTE.SuperGLUE_RTE_gen_ce346a import RTE_datasets
    from ..SuperGLUE_ReCoRD.SuperGLUE_ReCoRD_gen_d8f19c import ReCoRD_datasets
    from ..SuperGLUE_WiC.SuperGLUE_WiC_gen_c39367 import WiC_datasets
    from ..SuperGLUE_WSC.SuperGLUE_WSC_gen_d8d441 import WSC_datasets
    from ..race.race_gen_12de48 import race_datasets
    from ..Xsum.Xsum_gen_d2126e import Xsum_datasets
    from ..gsm8k.gsm8k_gen_2dd372 import gsm8k_datasets
    from ..summedits.summedits_gen_4f35b5 import summedits_datasets
    from ..math.math_gen_78bcba import math_datasets
    from ..TheoremQA.TheoremQA_gen_891fcf import TheoremQA_datasets
    from ..hellaswag.hellaswag_gen_cae9cb import hellaswag_datasets
    from ..ARC_e.ARC_e_gen_0a29bf import ARC_e_datasets
    from ..ARC_c.ARC_c_gen_3f3039 import ARC_c_datasets
    from ..commonsenseqa.commonsenseqa_gen_a58dbd import commonsenseqa_datasets
    from ..piqa.piqa_gen_8287ae import piqa_datasets
    from ..siqa.siqa_gen_a3c714 import siqa_datasets
    from ..strategyqa.strategyqa_gen_be3f8d import strategyqa_datasets
    from ..winogrande.winogrande_gen_c19d87 import winogrande_datasets
    from ..obqa.obqa_gen_b2cde9 import obqa_datasets
    from ..nq.nq_gen_a6ffca import nq_datasets
    from ..triviaqa.triviaqa_gen_cc3cbf import triviaqa_datasets
    from ..flores.flores_gen_8eb9ca import flores_datasets
    from ..crowspairs.crowspairs_gen_dd110a import crowspairs_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])

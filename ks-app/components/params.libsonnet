{
  global: {},
  components: {
    // Component-level parameters, defined initially from 'ks prototype use ...'
    // Each object below should correspond to a component in the components/ directory
    dotaservice: {
      agents: 16,
      batch_size: 8,
      dotaclient_image_tag: 'latest',
      dotaservice_image_tag: '0.3.6',
      epochs: 4,
      expname: 'exp2',
      jobname: 'job15',
      learning_rate: '1e-5',
      entropy_coef: '1e-4',
      max_dota_time: 600,
      optimizers: 1,
      pretrained_model: '',
      rollout_size: 9999,
      seq_len: 256,
      seq_per_epoch: 32,
    },
  },
}
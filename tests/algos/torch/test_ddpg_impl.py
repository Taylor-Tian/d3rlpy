import pytest

from d3rlpy.algos.torch.ddpg_impl import DDPGImpl
from d3rlpy.augmentation import AugmentationPipeline
from tests.algos.algo_test import torch_impl_tester, DummyScaler


@pytest.mark.parametrize('observation_shape', [(100, ), (4, 84, 84)])
@pytest.mark.parametrize('action_size', [2])
@pytest.mark.parametrize('actor_learning_rate', [1e-3])
@pytest.mark.parametrize('critic_learning_rate', [1e-3])
@pytest.mark.parametrize('gamma', [0.99])
@pytest.mark.parametrize('tau', [0.05])
@pytest.mark.parametrize('n_critics', [1])
@pytest.mark.parametrize('bootstrap', [False])
@pytest.mark.parametrize('share_encoder', [True])
@pytest.mark.parametrize('reguralizing_rate', [1e-8])
@pytest.mark.parametrize('eps', [1e-8])
@pytest.mark.parametrize('use_batch_norm', [True, False])
@pytest.mark.parametrize('q_func_type', ['mean', 'qr', 'iqn', 'fqf'])
@pytest.mark.parametrize('scaler', [None, DummyScaler()])
@pytest.mark.parametrize('augmentation', [AugmentationPipeline()])
@pytest.mark.parametrize('n_augmentations', [1])
@pytest.mark.parametrize('encoder_params', [{}])
def test_ddpg_impl(observation_shape, action_size, actor_learning_rate,
                   critic_learning_rate, gamma, tau, n_critics, bootstrap,
                   share_encoder, reguralizing_rate, eps, use_batch_norm,
                   q_func_type, scaler, augmentation, n_augmentations,
                   encoder_params):
    impl = DDPGImpl(observation_shape,
                    action_size,
                    actor_learning_rate,
                    critic_learning_rate,
                    gamma,
                    tau,
                    n_critics,
                    bootstrap,
                    share_encoder,
                    reguralizing_rate,
                    eps,
                    use_batch_norm,
                    q_func_type=q_func_type,
                    use_gpu=False,
                    scaler=scaler,
                    augmentation=augmentation,
                    n_augmentations=n_augmentations,
                    encoder_params=encoder_params)
    torch_impl_tester(impl,
                      discrete=False,
                      deterministic_best_action=q_func_type != 'iqn')

from gym.envs.registration import register

register(
    id='mytake-v0',
    entry_point='gym_count_blackjack.envs:mytakeEnv'
)

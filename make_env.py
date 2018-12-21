""""
Code for creating a multiagent environment with one of the scenarios listed
in ./scenarios/.
Can be called by using, for example:
    env = make_env('simple_speaker_listener')
After producing the env object, can be used similarly to an OpenAI gym
environment.
A policy using this environment must output actions in the form of a list
for all agents. Each element of the list should be a numpy array,
of size (env.world.dim_p + env.world.dim_c, 1). Physical actions precede
communication actions in this array. See environment.py for more details.
"""

def make_env(scenario_name, benchmark=False, discrete_action=True):
    '''
    Creates a MultiAgentEnv object as env. This can be used similar to a gym
    environment by calling env.reset() and env.step().
    Use env.render() to view the environment on the screen.
    Input:
        scenario_name   :   name of the scenario from ./scenarios/ to be Returns
                            (without the .py extension)
        benchmark       :   whether you want to produce benchmarking data
                            (usually only done during evaluation)
    Some useful env properties (see environment.py):
        .observation_space  :   Returns the observation space for each agent
        .action_space       :   Returns the action space for each agent
        .n                  :   Returns the number of Agents
    '''
    from multiagent.environment import MultiAgentEnv
    import multiagent.scenarios as scenarios

    # load scenario from script
    scenario = scenarios.load(scenario_name + ".py").Scenario()
    # create world
    world = scenario.make_world()
    # create multiagent environment
    if hasattr(scenario, 'post_step'):
        post_step = scenario.post_step
    else:
        post_step = None
    if benchmark:
        env = MultiAgentEnv(world, reset_callback=scenario.reset_world,
                            reward_callback=scenario.reward,
                            observation_callback=scenario.observation,
                            post_step_callback=post_step,
                            info_callback=scenario.benchmark_data,
                            discrete_action=discrete_action)
    else:
        env = MultiAgentEnv(world, reset_callback=scenario.reset_world,
                            reward_callback=scenario.reward,
                            observation_callback=scenario.observation,
                            post_step_callback=post_step,
                            discrete_action=discrete_action,
                            shared_viewer=False)
    return env


if __name__ == '__main__':
    import numpy as np
    import time
    env = make_env('simple')
    env.action_space
    env.discrete_action_input
    env.discrete_action_space


    s0 = env.reset()[0]
    time.sleep(1)
    # env.render(mode="human", close=False)
    print(s0)
    actions = np.eye(5)
    s1 = env.step([actions[1]])[0]
    env.agents[0].action.u
    for _ in range(5):
        s1 = env.step([actions[1]])[0]
    print(s1)
    time.sleep(3)
    env.render(mode="human", close=False)
    # env.close()
    # 0: nothing
    # 1: left
    # 2: right
    # 3: down
    # 4: up


    # import gym
    # gym.__version__
    # import numpy as np
    # ENV_NAME = 'CartPole-v0'
    # # Get the environment and extract the number of actions.
    # env = gym.make(ENV_NAME)
    # # env.render()
    # env.reset()
    # env.step(np.array(1))
    # env.render()
    # env.close()

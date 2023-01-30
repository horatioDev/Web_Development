# Github Actions

  1. Create .github/workflows/ dir to store workflow files

  2. In .github/workflows/ dir, create .yaml/.yml file: file_name.yml

  ## Components of GitHub Actions
    - GitHub Actions workflow to be triggered when an event occurs in your repository, such as a pull request being opened or an issue being created. Your workflow contains one or more jobs which can run in sequential order or in parallel. Each job will run inside its own virtual machine runner, or inside a container, and has one or more steps that either run a script that you define or run an action, which is a reusable extension that can simplify your workflow.

    ### Workflows
      - A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.

      - Workflows are defined in the .github/workflows directory in a repository, and a repository can have multiple workflows, each of which can perform a different set of tasks. For example, you can have one workflow to build and test pull requests, another workflow to deploy your application every time a release is created, and still another workflow that adds a label every time someone opens a new issue.

    ### Events
      - A job is a set of steps in a workflow that execute on the same runner. Each step is either a shell script that will be executed, or an action that will be run. Steps are executed in order and are dependent on each other. Since each step is executed on the same runner, you can share data from one step to another. For example, you can have a step that builds your application followed by a step that tests the application that was built.

      - You can configure a job's dependencies with other jobs; by default, jobs have no dependencies and run in parallel with each other. When a job takes a dependency on another job, it will wait for the dependent job to complete before it can run. For example, you may have multiple build jobs for different architectures that have no dependencies, and a packaging job that is dependent on those jobs. The build jobs will run in parallel, and when they have all completed successfully, the packaging job will run.

    ### Actions
      - An action is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task. Use an action to help reduce the amount of repetitive code that you write in your workflow files. An action can pull your git repository from GitHub, set up the correct toolchain for your build environment, or set up the authentication to your cloud provider.

      - You can write your own actions, or you can find actions to use in your workflows in the GitHub Marketplace.

    ### Runners
      - A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time. GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows; each workflow run executes in a fresh, newly-provisioned virtual machine. GitHub also offers larger runners, which are available in larger configurations.

  ## Workflow file
  ```
  name: Workflow name in github actions.

  on: Specifies the trigger for this workflow every time someone pushes a change to the repository or merges a pull request. When the workflow should run.

  jobs: Groups together all the jobs that run in the 'name:' workflow. Tasks to do when workflow is run.

    test_project: Defines a job named 'test_project'. The child keys will define properties of the job. Name of job.

      runs-on: Configures the job to run on the latest version of an Ubuntu Linux runner. This means that the job will execute on a fresh virtual machine hosted by GitHub. What machine code runs on..

      steps: Groups together all the steps that run in the 'test_project' job. Each item nested under this section is a separate action or shell script. What should happen

      - uses: The uses keyword specifies that this step will run 'v3' of the 'actions/checkout' action. This is an action that checks out your repository onto the runner, allowing you to run scripts or other actions against your code (such as build and test tools). You should use the checkout action any time your workflow will run against the repository's code. Action written by github.

      - name: Description of step taking place.
        run: The run keyword tells the job to execute a command on the runner. Requirements need to run app.

  ```
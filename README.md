# StepFunctions Enrichment Demo

This demo showcases a StepFunctions orchestration and is packaged and deploy using [AWS SAM](https://aws.amazon.com/serverless/sam/). The orchestration assumes that a business event has occured and an appropriately formed event has triggered a rule on EventBridge. The StepFunction execution then mocks a set of systems retrieving gradually more information about the input, including a Parallel execution step.

> Note: all integrations from the Action steps in the StepFunctions state machine, i.e. Lambda -> downstream system and S3 interaction is mocked within the Lambda functions.

AWS X-Ray tracing and CloudWatch Logs have been enabled for StepFunctions so that you can examine the working and state transitions verbosely.

The Lambda functions used in this demo make use of AWS Graviton processors - [find out more](https://aws.amazon.com/ec2/graviton/)

## Deployment

1. Ensure you have the [AWS CLI](https://aws.amazon.com/cli/) and [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed.
2. Clone this repo locally with `git clone https://github.com/benjymoses/stepfunctions-enrichment.git`
3. Ensure you have an AWS profile configured on your system with `aws configure` at your terminal. See: [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
4. Run `sam build` to ensure all build artefacts and their dependencies are satisfied.
5. Run `sam deploy --guided` and follow the instructions. Run `sam deploy --guided --profile awsProfileName` if you need to use a named AWS CLI profile.

## Usage

You can use the [StepFunctions Console](https://console.aws.amazon.com/states) and manually start an execution by following [these instructions](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started.html#start-new-execution). Any input event will result in success, including the default one the console presents.

Alternatively, you can see how an execution might take place with an EventBridge Event.

#### Event Bridge

1. From the Amazon [EventBridge Console](https://console.aws.amazon.com/events) click on **Event buses**
2. Click **Send events** in the top right corner.
3. Ensure the "default" event bus is selected then fill in the following information:

**Event Source**: `demo.pos`

**Detail Type**: `sale` (any value will actually work in this demo)

**Event Detail**: `{ "action": "create-receipt" }`

4. Click **Send**

You can now see in the StepFunctions console that an execution has taken place. If you examine the *Input* tab of the first *node* for that execution you will see the metadata that StepFunctions received from EventBridge.


## Clean up

Once you have finished experimenting you can clean up all resources created so that you don't incur ongoing costs. Assuming that you still still have valid AWS credentials from the deployment instructions above you can run:

```
sam delete
``` 

and follow the instructions.

## More reading

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

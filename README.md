
# AWS CDK: Now I Get It

This [AWS Cloud Development Kit (CDK)(https://aws.amazon.com/cdk/) app is
the companion code for the blog post
[AWS CDK: Now I Get It](https://www.packetmischief.ca).

The primary bits of interest which align to the blog are:

- Composing and sharing:
  [cdk_now_i_get_it_v1_stack.py](cdk_now_i_get_it/cdk_now_i_get_it_v1_stack.py)
- Native language:
  [cdk_now_i_get_it_v2_stack.py](cdk_now_i_get_it/cdk_now_i_get_it_v2_stack.py)
- Proven defaults:
  [cdk_now_i_get_it_v3_stack.py](cdk_now_i_get_it/cdk_now_i_get_it_v3_stack.py)
- The app which consumes the above constructs: [app.py](app.py)

The original CDK README is below in case you need a little help getting going.

## Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the
following step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

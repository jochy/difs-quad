
def after_step(context, step):
    if step.status == 'failed':
        context.driver.save_screenshot("screenshot.png")
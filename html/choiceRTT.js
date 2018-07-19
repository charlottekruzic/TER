/****************** 
 * Choicertt Test *
 ******************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});
var my = psychoJS;

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new Color([0, 0, 0]),
  units: 'height'
});

// store info about the experiment session:
my.expName = 'choiceRTT';  // from the Builder filename that created this script
my.expInfo = {'participant': '', 'session': '001'};


// set up the experiment:
psychoJS.schedule(setupExperiment);

// register all available resources and download them:
psychoJS.scheduleResources();

// dialog box:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: my.expInfo,
  title: my.expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(() => (psychoJS.gui.dialogComponent.button === 'OK'), flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin);
flowScheduler.add(instructionsRoutineEachFrame);
flowScheduler.add(instructionsRoutineEnd);
const practiceTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceTrialsLoopBegin, practiceTrialsLoopScheduler);
flowScheduler.add(practiceTrialsLoopScheduler);
flowScheduler.add(practiceTrialsLoopEnd);
flowScheduler.add(startTaskRoutineBegin);
flowScheduler.add(startTaskRoutineEachFrame);
flowScheduler.add(startTaskRoutineEnd);
const mainTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(mainTrialsLoopBegin, mainTrialsLoopScheduler);
flowScheduler.add(mainTrialsLoopScheduler);
flowScheduler.add(mainTrialsLoopEnd);
flowScheduler.add(thanksRoutineBegin);
flowScheduler.add(thanksRoutineEachFrame);
flowScheduler.add(thanksRoutineEnd);
flowScheduler.add(quitPsychoJS);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS);

psychoJS.start();


function setupExperiment() {
  if (psychoJS.status === PsychoJS.Status.NOT_CONFIGURED) {
    psychoJS.status = PsychoJS.Status.CONFIGURING;

    psychoJS.configure('config.json')
    .then( config => {

      // An ExperimentHandler isn't essential but helps with data saving
      psychoJS.experiment = new ExperimentHandler({extraInfo: my.expInfo});

      /*
      // logging:
      my.logger.console.setLevel(psychoJS.logging.WARNING);
      my.logger.server.set({'level':psychoJS.logging.WARNING, 'saveTo':'EXPERIMENT_SERVER', 'experimentInfo': my.expInfo});*/

      // change status to leave setupExperiment loop:
      psychoJS.status = PsychoJS.Status.CONFIGURED;
    });
  }

  // the loop will return until the configuration is completed
  // at which point the status changes to CONFIGURED
  if (psychoJS.status === PsychoJS.Status.CONFIGURED) {
    psychoJS.status = PsychoJS.Status.STARTED;
    return Scheduler.Event.NEXT;
  } else
    return Scheduler.Event.FLIP_REPEAT;
}

function updateInfo() {
  my.expInfo['date'] = MonotonicClock.getDateStr();  // add a simple timestamp
  my.expInfo['expName'] = my.expName;

  // store frame rate of monitor if we can measure it successfully
  my.expInfo['frameRate'] = my.window.getActualFrameRate();
  if (typeof my.expInfo['frameRate'] !== 'undefined')
    my.frameDur = 1.0/Math.round(my.expInfo['frameRate']);
  else
    my.frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  addInfoFromUrl(my.expInfo);

  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "instructions"
  my.instructionsClock = new Clock();
  my.instr = new TextStim({
    win : my.window,
    name : 'my.instr',
    text : "In this task you will push the space bar whenever you see the target 'X' appear.\n\nFirst, we shall have a practice.\n\nPush space bar to begin the practice session.",
    font : 'Arial',
    units : 'height',   pos : [0, 0], height : 0.04,  wrapWidth : undefined, ori: 0,
    color : new Color('white'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "main"
  my.mainClock = new Clock();
  my.pos1 = new ImageStim({
    win : my.window,
    name : 'my.pos1', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  my.pos2 = new ImageStim({
    win : my.window,
    name : 'my.pos2', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  my.pos3 = new ImageStim({
    win : my.window,
    name : 'my.pos3', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  my.pos4 = new ImageStim({
    win : my.window,
    name : 'my.pos4', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  my.targImage = new ImageStim({
    win : my.window,
    name : 'my.targImage', units : 'height', 
    image : 'tarX.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "startTask"
  my.startTaskClock = new Clock();
  my.ready = new TextStim({
    win : my.window,
    name : 'my.ready',
    text : 'Now we shall begin the actual experiment.\n\nReady?\n\nPush space bar to begin.',
    font : 'Arial',
    units : 'height',   pos : [0, 0], height : 0.04,  wrapWidth : undefined, ori: 0,
    color : new Color('white'),  opacity : 1,
    depth : 0.0 
  });
  
  // Initialize components for Routine "main"
  my.mainClock = new Clock();
  my.pos1 = new ImageStim({
    win : my.window,
    name : 'my.pos1', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  my.pos2 = new ImageStim({
    win : my.window,
    name : 'my.pos2', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  my.pos3 = new ImageStim({
    win : my.window,
    name : 'my.pos3', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  my.pos4 = new ImageStim({
    win : my.window,
    name : 'my.pos4', units : 'height', 
    image : 'plainWhite.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  my.targImage = new ImageStim({
    win : my.window,
    name : 'my.targImage', units : 'height', 
    image : 'tarX.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new Color ([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "thanks"
  my.thanksClock = new Clock();
  my.text = new TextStim({
    win : my.window,
    name : 'my.text',
    text : 'Thanks you for participanting!\n\nThe experiment is now over.',
    font : 'Arial',
    units : 'height',   pos : [0, 0], height : 0.05,  wrapWidth : undefined, ori: 0,
    color : new Color('white'),  opacity : 1,
    depth : 0.0 
  });
  
  // Create some handy timers
  my.globalClock = new Clock();  // to track the time since experiment started
  my.routineTimer = new CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function instructionsRoutineBegin() {
  //------Prepare to start Routine 'instructions'-------
  my.t = 0;
  my.instructionsClock.reset(); // clock
  my.frameN = -1;
  // update component parameters for each repeat
  my.startInst = new BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  my.instructionsComponents = [];
  my.instructionsComponents.push(my.instr);
  my.instructionsComponents.push(my.startInst);
  
  for (const thisComponent of my.instructionsComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function instructionsRoutineEachFrame() {
  //------Loop for each frame of Routine 'instructions'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  my.t = my.instructionsClock.getTime();
  my.frameN = my.frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *my.instr* updates
  if (my.t >= 0.0 && my.instr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.instr.tStart = my.t;  // (not accounting for frame time here)
    my.instr.frameNStart = my.frameN;  // exact frame index
    my.instr.setAutoDraw(true);
  }
  
  // *my.startInst* updates
  if (my.t >= 0.0 && my.startInst.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.startInst.tStart = my.t;  // (not accounting for frame time here)
    my.startInst.frameNStart = my.frameN;  // exact frame index
    my.startInst.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    my.eventManager.clearEvents({eventType:'keyboard'});
  }
  if (my.startInst.status === PsychoJS.Status.STARTED) {
    let theseKeys = my.eventManager.getKeys();
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of my.instructionsComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function instructionsRoutineEnd() {
  //------Ending Routine 'instructions'-------
  for (const thisComponent of my.instructionsComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
  my.routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function practiceTrialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  my.practiceTrials = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: my.expInfo, originPath: undefined,
    trialList: 'srttPractice.xlsx',
    seed: undefined, name: 'my.practiceTrials'});
  psychoJS.experiment.addLoop(my.practiceTrials); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisPracticeTrial of my.practiceTrials) {
    thisScheduler.add(importTrialAttributes(thisPracticeTrial));
    thisScheduler.add(mainRoutineBegin);
    thisScheduler.add(mainRoutineEachFrame);
    thisScheduler.add(mainRoutineEnd);
    thisScheduler.add(endLoopIteration(thisPracticeTrial));
  }

  return Scheduler.Event.NEXT;
}

function practiceTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(my.practiceTrials);
  psychoJS.experiment.save({
    attributes: my.practiceTrials.getAttributes()
  });

  return Scheduler.Event.NEXT;
}

function mainTrialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  my.mainTrials = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.FULLRANDOM,
    extraInfo: my.expInfo, originPath: undefined,
    trialList: 'srttConditions.xlsx',
    seed: undefined, name: 'my.mainTrials'});
  psychoJS.experiment.addLoop(my.mainTrials); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisMainTrial of my.mainTrials) {
    thisScheduler.add(importTrialAttributes(thisMainTrial));
    thisScheduler.add(mainRoutineBegin);
    thisScheduler.add(mainRoutineEachFrame);
    thisScheduler.add(mainRoutineEnd);
    thisScheduler.add(endLoopIteration(thisMainTrial));
  }

  return Scheduler.Event.NEXT;
}

function mainTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(my.mainTrials);
  psychoJS.experiment.save({
    attributes: my.mainTrials.getAttributes()
  });

  return Scheduler.Event.NEXT;
}

function mainRoutineBegin() {
  //------Prepare to start Routine 'main'-------
  my.t = 0;
  my.mainClock.reset(); // clock
  my.frameN = -1;
  // update component parameters for each repeat
  my.pos1.setPos([(- 0.375), 0]);
  my.pos2.setPos([(- 0.125), 0]);
  my.pos3.setPos([0.125, 0]);
  my.pos4.setPos([0.375, 0]);
  my.targImage.setPos([my.xPos, 0]);
  my.response = new BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  my.mainComponents = [];
  my.mainComponents.push(my.pos1);
  my.mainComponents.push(my.pos2);
  my.mainComponents.push(my.pos3);
  my.mainComponents.push(my.pos4);
  my.mainComponents.push(my.targImage);
  my.mainComponents.push(my.response);
  
  for (const thisComponent of my.mainComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function mainRoutineEachFrame() {
  //------Loop for each frame of Routine 'main'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  my.t = my.mainClock.getTime();
  my.frameN = my.frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *my.pos1* updates
  if (my.t >= 0 && my.pos1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.pos1.tStart = my.t;  // (not accounting for frame time here)
    my.pos1.frameNStart = my.frameN;  // exact frame index
    my.pos1.setAutoDraw(true);
  }
  
  // *my.pos2* updates
  if (my.t >= 0 && my.pos2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.pos2.tStart = my.t;  // (not accounting for frame time here)
    my.pos2.frameNStart = my.frameN;  // exact frame index
    my.pos2.setAutoDraw(true);
  }
  
  // *my.pos3* updates
  if (my.t >= 0 && my.pos3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.pos3.tStart = my.t;  // (not accounting for frame time here)
    my.pos3.frameNStart = my.frameN;  // exact frame index
    my.pos3.setAutoDraw(true);
  }
  
  // *my.pos4* updates
  if (my.t >= 0 && my.pos4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.pos4.tStart = my.t;  // (not accounting for frame time here)
    my.pos4.frameNStart = my.frameN;  // exact frame index
    my.pos4.setAutoDraw(true);
  }
  
  // *my.targImage* updates
  if (my.t >= my.isi && my.targImage.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.targImage.tStart = my.t;  // (not accounting for frame time here)
    my.targImage.frameNStart = my.frameN;  // exact frame index
    my.targImage.setAutoDraw(true);
  }
  
  // *my.response* updates
  if (my.t >= my.isi && my.response.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.response.tStart = my.t;  // (not accounting for frame time here)
    my.response.frameNStart = my.frameN;  // exact frame index
    my.response.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    my.response.clock.reset();  // now t=0
    my.eventManager.clearEvents({eventType:'keyboard'});
  }
  if (my.response.status === PsychoJS.Status.STARTED) {
    let theseKeys = my.eventManager.getKeys({keyList:['c', 'v', 'b', 'n']});
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      my.response.keys = theseKeys[theseKeys.length-1]  // just the last key pressed
      my.response.rt = my.response.clock.getTime();
      // was this 'correct'?
      if (my.response.keys == my.corrAns) {
          my.response.corr = 1;
      } else {
          my.response.corr = 0;
      }
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of my.mainComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function mainRoutineEnd() {
  //------Ending Routine 'main'-------
  for (const thisComponent of my.mainComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // check responses
  if (['', [], undefined].indexOf(my.response.keys) >= 0) {    // No response was made
      my.response.keys = undefined;
  }
  // was no response the correct answer?!
  if (my.response.keys == undefined) {
    if (psychoJS.str(my.corrAns).toLowerCase() == 'none') {
       my.response.corr = 1  // correct non-response
    } else {
       my.response.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for my.thisExp (ExperimentHandler)
  my.experiment.addData('my.response.keys', my.response.keys);
  my.experiment.addData('my.response.corr', my.response.corr);
  if (my.response.keys != undefined) {  // we had a response
      my.experiment.addData('my.response.rt', my.response.rt);
      my.routineTimer.reset();
      }
  // the Routine "main" was not non-slip safe, so reset the non-slip timer
  my.routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function startTaskRoutineBegin() {
  //------Prepare to start Routine 'startTask'-------
  my.t = 0;
  my.startTaskClock.reset(); // clock
  my.frameN = -1;
  // update component parameters for each repeat
  my.go = new BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  my.startTaskComponents = [];
  my.startTaskComponents.push(my.ready);
  my.startTaskComponents.push(my.go);
  
  for (const thisComponent of my.startTaskComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function startTaskRoutineEachFrame() {
  //------Loop for each frame of Routine 'startTask'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  my.t = my.startTaskClock.getTime();
  my.frameN = my.frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *my.ready* updates
  if (my.t >= 0.0 && my.ready.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.ready.tStart = my.t;  // (not accounting for frame time here)
    my.ready.frameNStart = my.frameN;  // exact frame index
    my.ready.setAutoDraw(true);
  }
  
  // *my.go* updates
  if (my.t >= 0.0 && my.go.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.go.tStart = my.t;  // (not accounting for frame time here)
    my.go.frameNStart = my.frameN;  // exact frame index
    my.go.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    my.eventManager.clearEvents({eventType:'keyboard'});
  }
  if (my.go.status === PsychoJS.Status.STARTED) {
    let theseKeys = my.eventManager.getKeys();
    
    // check for quit:
    if ("escape" in theseKeys) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of my.startTaskComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function startTaskRoutineEnd() {
  //------Ending Routine 'startTask'-------
  for (const thisComponent of my.startTaskComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "startTask" was not non-slip safe, so reset the non-slip timer
  my.routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

function thanksRoutineBegin() {
  //------Prepare to start Routine 'thanks'-------
  my.t = 0;
  my.thanksClock.reset(); // clock
  my.frameN = -1;
  my.routineTimer.add(5.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  my.thanksComponents = [];
  my.thanksComponents.push(my.text);
  
  for (const thisComponent of my.thanksComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

function thanksRoutineEachFrame() {
  //------Loop for each frame of Routine 'thanks'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  my.t = my.thanksClock.getTime();
  my.frameN = my.frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *my.text* updates
  if (my.t >= 0.0 && my.text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    my.text.tStart = my.t;  // (not accounting for frame time here)
    my.text.frameNStart = my.frameN;  // exact frame index
    my.text.setAutoDraw(true);
  }
  my.frameRemains = 0.0 + 5 - my.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (my.text.status === PsychoJS.Status.STARTED && my.t >= my.frameRemains) {
    my.text.setAutoDraw(false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of my.thanksComponents)
    if ('status' in thisComponent && thisComponent.status != PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    psychoJS.quit('The [Escape] key was pressed. Goodbye!');
  }
  
  // refresh the screen if continuing
  if (continueRoutine && my.routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}

function thanksRoutineEnd() {
  //------Ending Routine 'thanks'-------
  for (const thisComponent of my.thanksComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

function endLoopIteration(thisTrial) {
  // ------Prepare for next entry------
  return function () {
    if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      my.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}

function importTrialAttributes(thisTrial) {
  return function () {
    psychoJS.importAttributes(thisTrial);

    return Scheduler.Event.NEXT;
  };
}

function quitPsychoJS() {
  my.window.close();
  psychoJS.quit();

  return Scheduler.Event.QUIT;
}

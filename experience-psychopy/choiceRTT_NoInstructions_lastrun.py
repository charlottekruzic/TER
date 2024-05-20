﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Wed Feb 21 15:26:39 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'choice_RTT_demo'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/axel/software/Gitlab/Pavlovia/Choice_RT/choicertt/choiceRTT_NoInstructions_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1440, 900], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[1, 1, 1], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1, 1, 1]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='ptb')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='PsychToolbox')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "trial" ---
    rightright_tile = visual.ImageStim(
        win=win,
        name='rightright_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.375, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    right_tile = visual.ImageStim(
        win=win,
        name='right_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.125, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    left_tile = visual.ImageStim(
        win=win,
        name='left_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.125, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    leftleft_tile = visual.ImageStim(
        win=win,
        name='leftleft_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.375, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    square_button = visual.ImageStim(
        win=win,
        name='square_button', 
        image='images/response_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    plus_button = visual.ImageStim(
        win=win,
        name='plus_button', 
        image='images/response_plus.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    cross_button = visual.ImageStim(
        win=win,
        name='cross_button', 
        image='images/response_cross.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    targetImage = visual.ImageStim(
        win=win,
        name='targetImage', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-8.0)
    keyResp = keyboard.Keyboard()
    mouseResp = event.Mouse(win=win)
    x, y = [None, None]
    mouseResp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial_feedback" ---
    text_fb = visual.TextStim(win=win, name='text_fb',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    moveOnKeys = keyboard.Keyboard()
    moveOnMouse = event.Mouse(win=win)
    x, y = [None, None]
    moveOnMouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "mainTrial_instruct" ---
    main_trial_instruct = visual.TextStim(win=win, name='main_trial_instruct',
        text='Well done, that’s the practice over!\n\nNow for the main experiment.\n\nClick / tap / press space to continue!',
        font='Arial',
        pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    ready_button = visual.ImageStim(
        win=win,
        name='ready_button', 
        image='images/response_ready.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "trial" ---
    rightright_tile = visual.ImageStim(
        win=win,
        name='rightright_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.375, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    right_tile = visual.ImageStim(
        win=win,
        name='right_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.125, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    left_tile = visual.ImageStim(
        win=win,
        name='left_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.125, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    leftleft_tile = visual.ImageStim(
        win=win,
        name='leftleft_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.375, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    square_button = visual.ImageStim(
        win=win,
        name='square_button', 
        image='images/response_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    plus_button = visual.ImageStim(
        win=win,
        name='plus_button', 
        image='images/response_plus.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    cross_button = visual.ImageStim(
        win=win,
        name='cross_button', 
        image='images/response_cross.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    targetImage = visual.ImageStim(
        win=win,
        name='targetImage', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-8.0)
    keyResp = keyboard.Keyboard()
    mouseResp = event.Mouse(win=win)
    x, y = [None, None]
    mouseResp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "end_message" ---
    end_text = visual.TextStim(win=win, name='end_text',
        text='That’s the experiment finished!\n\nThanks for your time. You’ve earned a cup of tea.',
        font='Arial',
        pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # set up handler to look after randomisation of conditions etc
    PracticeLoop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('RTtimeConditions_own.xlsx'),
        seed=None, name='PracticeLoop')
    thisExp.addLoop(PracticeLoop)  # add the loop to the experiment
    thisPracticeLoop = PracticeLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            globals()[paramName] = thisPracticeLoop[paramName]
    
    for thisPracticeLoop in PracticeLoop:
        currentLoop = PracticeLoop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
        if thisPracticeLoop != None:
            for paramName in thisPracticeLoop:
                globals()[paramName] = thisPracticeLoop[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        # Run 'Begin Routine' code from setStimuli
        positionList = [-0.375,-0.125,0.125,0.375] #list of possible X coordinates for target to appear
        shuffle(positionList) #randomise these positions
        targetX = positionList[0] #pick the first value from the list 
        
        #thisImage is the variable in the Image field of targetImage
        if thisImage == 'images/target_square.jpg': #path of where to find the target image
            corrAns = 'v' #setting the key press that will be the correct answer
            corrButton = square_button #setting the button that will be the correct answer
            corrButtonName = 'square_button' #making this a string so that it can be compared later when checking for acccuracy
        elif thisImage == 'images/target_cross.jpg':
            corrAns = 'c'
            corrButton = cross_button
            corrButtonName = 'cross_button'
        elif thisImage == 'images/target_plus.jpg':
            corrAns = 'b'
            corrButton = plus_button
            corrButtonName = 'plus_button'
        
        
        targetImage.setPos([targetX, 0])
        targetImage.setImage(thisImage)
        keyResp.keys = []
        keyResp.rt = []
        _keyResp_allKeys = []
        # setup some python lists for storing info about the mouseResp
        mouseResp.x = []
        mouseResp.y = []
        mouseResp.leftButton = []
        mouseResp.midButton = []
        mouseResp.rightButton = []
        mouseResp.time = []
        mouseResp.clicked_name = []
        gotValidClick = False  # until a click is received
        mouseResp.mouseClock.reset()
        # keep track of which components have finished
        trialComponents = [rightright_tile, right_tile, left_tile, leftleft_tile, square_button, plus_button, cross_button, targetImage, keyResp, mouseResp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rightright_tile* updates
            
            # if rightright_tile is starting this frame...
            if rightright_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                rightright_tile.frameNStart = frameN  # exact frame index
                rightright_tile.tStart = t  # local t and not account for scr refresh
                rightright_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightright_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                rightright_tile.status = STARTED
                rightright_tile.setAutoDraw(True)
            
            # if rightright_tile is active this frame...
            if rightright_tile.status == STARTED:
                # update params
                pass
            
            # *right_tile* updates
            
            # if right_tile is starting this frame...
            if right_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                right_tile.frameNStart = frameN  # exact frame index
                right_tile.tStart = t  # local t and not account for scr refresh
                right_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                right_tile.status = STARTED
                right_tile.setAutoDraw(True)
            
            # if right_tile is active this frame...
            if right_tile.status == STARTED:
                # update params
                pass
            
            # *left_tile* updates
            
            # if left_tile is starting this frame...
            if left_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                left_tile.frameNStart = frameN  # exact frame index
                left_tile.tStart = t  # local t and not account for scr refresh
                left_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                left_tile.status = STARTED
                left_tile.setAutoDraw(True)
            
            # if left_tile is active this frame...
            if left_tile.status == STARTED:
                # update params
                pass
            
            # *leftleft_tile* updates
            
            # if leftleft_tile is starting this frame...
            if leftleft_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                leftleft_tile.frameNStart = frameN  # exact frame index
                leftleft_tile.tStart = t  # local t and not account for scr refresh
                leftleft_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftleft_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                leftleft_tile.status = STARTED
                leftleft_tile.setAutoDraw(True)
            
            # if leftleft_tile is active this frame...
            if leftleft_tile.status == STARTED:
                # update params
                pass
            
            # *square_button* updates
            
            # if square_button is starting this frame...
            if square_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                square_button.frameNStart = frameN  # exact frame index
                square_button.tStart = t  # local t and not account for scr refresh
                square_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                square_button.status = STARTED
                square_button.setAutoDraw(True)
            
            # if square_button is active this frame...
            if square_button.status == STARTED:
                # update params
                pass
            
            # *plus_button* updates
            
            # if plus_button is starting this frame...
            if plus_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                plus_button.frameNStart = frameN  # exact frame index
                plus_button.tStart = t  # local t and not account for scr refresh
                plus_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(plus_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                plus_button.status = STARTED
                plus_button.setAutoDraw(True)
            
            # if plus_button is active this frame...
            if plus_button.status == STARTED:
                # update params
                pass
            
            # *cross_button* updates
            
            # if cross_button is starting this frame...
            if cross_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                cross_button.frameNStart = frameN  # exact frame index
                cross_button.tStart = t  # local t and not account for scr refresh
                cross_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                cross_button.status = STARTED
                cross_button.setAutoDraw(True)
            
            # if cross_button is active this frame...
            if cross_button.status == STARTED:
                # update params
                pass
            
            # *targetImage* updates
            
            # if targetImage is starting this frame...
            if targetImage.status == NOT_STARTED and tThisFlip >= onsetTime-frameTolerance:
                # keep track of start time/frame for later
                targetImage.frameNStart = frameN  # exact frame index
                targetImage.tStart = t  # local t and not account for scr refresh
                targetImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(targetImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'targetImage.started')
                # update status
                targetImage.status = STARTED
                targetImage.setAutoDraw(True)
            
            # if targetImage is active this frame...
            if targetImage.status == STARTED:
                # update params
                pass
            
            # if targetImage is stopping this frame...
            if targetImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > targetImage.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    targetImage.tStop = t  # not accounting for scr refresh
                    targetImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targetImage.stopped')
                    # update status
                    targetImage.status = FINISHED
                    targetImage.setAutoDraw(False)
            
            # *keyResp* updates
            
            # if keyResp is starting this frame...
            if keyResp.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                keyResp.frameNStart = frameN  # exact frame index
                keyResp.tStart = t  # local t and not account for scr refresh
                keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                keyResp.status = STARTED
                # keyboard checking is just starting
                keyResp.clock.reset()  # now t=0
                keyResp.clearEvents(eventType='keyboard')
            if keyResp.status == STARTED:
                theseKeys = keyResp.getKeys(keyList=['b','c','v'], ignoreKeys=["escape"], waitRelease=False)
                _keyResp_allKeys.extend(theseKeys)
                if len(_keyResp_allKeys):
                    keyResp.keys = _keyResp_allKeys[-1].name  # just the last key pressed
                    keyResp.rt = _keyResp_allKeys[-1].rt
                    keyResp.duration = _keyResp_allKeys[-1].duration
                    # was this correct?
                    if (keyResp.keys == str(corrAns)) or (keyResp.keys == corrAns):
                        keyResp.corr = 1
                    else:
                        keyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *mouseResp* updates
            
            # if mouseResp is starting this frame...
            if mouseResp.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouseResp.frameNStart = frameN  # exact frame index
                mouseResp.tStart = t  # local t and not account for scr refresh
                mouseResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouseResp.status = STARTED
                prevButtonState = mouseResp.getPressed()  # if button is down already this ISN'T a new click
            if mouseResp.status == STARTED:  # only update if started and not finished!
                buttons = mouseResp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([square_button, plus_button, cross_button], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseResp):
                                gotValidClick = True
                                mouseResp.clicked_name.append(obj.name)
                        x, y = mouseResp.getPos()
                        mouseResp.x.append(x)
                        mouseResp.y.append(y)
                        buttons = mouseResp.getPressed()
                        mouseResp.leftButton.append(buttons[0])
                        mouseResp.midButton.append(buttons[1])
                        mouseResp.rightButton.append(buttons[2])
                        mouseResp.time.append(mouseResp.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # check responses
        if keyResp.keys in ['', [], None]:  # No response was made
            keyResp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               keyResp.corr = 1;  # correct non-response
            else:
               keyResp.corr = 0;  # failed to respond (incorrectly)
        # store data for PracticeLoop (TrialHandler)
        PracticeLoop.addData('keyResp.keys',keyResp.keys)
        PracticeLoop.addData('keyResp.corr', keyResp.corr)
        if keyResp.keys != None:  # we had a response
            PracticeLoop.addData('keyResp.rt', keyResp.rt)
            PracticeLoop.addData('keyResp.duration', keyResp.duration)
        # store data for PracticeLoop (TrialHandler)
        PracticeLoop.addData('mouseResp.x', mouseResp.x)
        PracticeLoop.addData('mouseResp.y', mouseResp.y)
        PracticeLoop.addData('mouseResp.leftButton', mouseResp.leftButton)
        PracticeLoop.addData('mouseResp.midButton', mouseResp.midButton)
        PracticeLoop.addData('mouseResp.rightButton', mouseResp.rightButton)
        PracticeLoop.addData('mouseResp.time', mouseResp.time)
        PracticeLoop.addData('mouseResp.clicked_name', mouseResp.clicked_name)
        # Run 'End Routine' code from recordRTandAccuracy
        #this code is to record the reaction times and accuracy of the trial
        
        thisRoutineDuration = t # how long did this trial last
        
        # keyResp.rt is the time with which a key was pressed
        # mouseResp.time is the time with which a button was clicked/pressed
        # thisRecRT - how long it took for participants to respond after onset of targetImage
        # thisRespType - keeping track of which response component was used
        # thisAcc - whether or not the response was correct
        # correctMouseResp - name of column in data output which records the accuracy of mouse responses
        
        if keyResp.keys:
            thisRespType = 'keyboard' #record type of response 
            thisRecRT = keyResp.rt - onsetTime #record time taken to response
            if keyResp.corr == 1: #if the response is correct
                thisAcc = 'correct' #print correct
            else:
                thisAcc = 'incorrect'
        else:
            thisRespType = 'mouse'
            thisRecRT = mouseResp.time[0] - onsetTime
            if mouseResp.clicked_name[0] == corrButtonName: #check if what was clicked corresponds to the correct button
                thisAcc = 'correct'
                thisExp.addData('correctMouseResp', 1) #record accuracy of mouse clicks
            else:
                thisAcc = 'incorrect'
                thisExp.addData('correctMouseResp', 0)
        
        thisExp.addData('trialRespTimes', thisRecRT) #record the actual response times of each trial
        
        
        #print(thisRoutineDuration, thisRecRT, thisRespType, thisAcc, onsetTime)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial_feedback.started', globalClock.getTime())
        text_fb.setText("The duration of the last routine was: "  + str(round(thisRoutineDuration, 3)) + " \nThe last recorded RT was: "  + str(round(thisRecRT, 3)) + " \nThe response type was: "  + thisRespType + " \nThe response was: "  + thisAcc + " \n\nPress or click to continue."  )
        moveOnKeys.keys = []
        moveOnKeys.rt = []
        _moveOnKeys_allKeys = []
        # setup some python lists for storing info about the moveOnMouse
        gotValidClick = False  # until a click is received
        moveOnMouse.mouseClock.reset()
        # keep track of which components have finished
        trial_feedbackComponents = [text_fb, moveOnKeys, moveOnMouse]
        for thisComponent in trial_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_fb* updates
            
            # if text_fb is starting this frame...
            if text_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_fb.frameNStart = frameN  # exact frame index
                text_fb.tStart = t  # local t and not account for scr refresh
                text_fb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_fb, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_fb.started')
                # update status
                text_fb.status = STARTED
                text_fb.setAutoDraw(True)
            
            # if text_fb is active this frame...
            if text_fb.status == STARTED:
                # update params
                pass
            
            # *moveOnKeys* updates
            waitOnFlip = False
            
            # if moveOnKeys is starting this frame...
            if moveOnKeys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moveOnKeys.frameNStart = frameN  # exact frame index
                moveOnKeys.tStart = t  # local t and not account for scr refresh
                moveOnKeys.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moveOnKeys, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'moveOnKeys.started')
                # update status
                moveOnKeys.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(moveOnKeys.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(moveOnKeys.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if moveOnKeys.status == STARTED and not waitOnFlip:
                theseKeys = moveOnKeys.getKeys(keyList=['c','v','b','space'], ignoreKeys=["escape"], waitRelease=False)
                _moveOnKeys_allKeys.extend(theseKeys)
                if len(_moveOnKeys_allKeys):
                    moveOnKeys.keys = _moveOnKeys_allKeys[-1].name  # just the last key pressed
                    moveOnKeys.rt = _moveOnKeys_allKeys[-1].rt
                    moveOnKeys.duration = _moveOnKeys_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # *moveOnMouse* updates
            
            # if moveOnMouse is starting this frame...
            if moveOnMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                moveOnMouse.frameNStart = frameN  # exact frame index
                moveOnMouse.tStart = t  # local t and not account for scr refresh
                moveOnMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(moveOnMouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('moveOnMouse.started', t)
                # update status
                moveOnMouse.status = STARTED
                prevButtonState = moveOnMouse.getPressed()  # if button is down already this ISN'T a new click
            if moveOnMouse.status == STARTED:  # only update if started and not finished!
                buttons = moveOnMouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # end routine on response            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_feedback" ---
        for thisComponent in trial_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial_feedback.stopped', globalClock.getTime())
        # check responses
        if moveOnKeys.keys in ['', [], None]:  # No response was made
            moveOnKeys.keys = None
        PracticeLoop.addData('moveOnKeys.keys',moveOnKeys.keys)
        if moveOnKeys.keys != None:  # we had a response
            PracticeLoop.addData('moveOnKeys.rt', moveOnKeys.rt)
            PracticeLoop.addData('moveOnKeys.duration', moveOnKeys.duration)
        # store data for PracticeLoop (TrialHandler)
        # the Routine "trial_feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'PracticeLoop'
    
    
    # --- Prepare to start Routine "mainTrial_instruct" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('mainTrial_instruct.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    mainTrial_instructComponents = [main_trial_instruct, key_resp, mouse, ready_button]
    for thisComponent in mainTrial_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "mainTrial_instruct" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *main_trial_instruct* updates
        
        # if main_trial_instruct is starting this frame...
        if main_trial_instruct.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            main_trial_instruct.frameNStart = frameN  # exact frame index
            main_trial_instruct.tStart = t  # local t and not account for scr refresh
            main_trial_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_trial_instruct, 'tStartRefresh')  # time at next scr refresh
            # update status
            main_trial_instruct.status = STARTED
            main_trial_instruct.setAutoDraw(True)
        
        # if main_trial_instruct is active this frame...
        if main_trial_instruct.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # end routine on response        
        # *ready_button* updates
        
        # if ready_button is starting this frame...
        if ready_button.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            ready_button.frameNStart = frameN  # exact frame index
            ready_button.tStart = t  # local t and not account for scr refresh
            ready_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ready_button, 'tStartRefresh')  # time at next scr refresh
            # update status
            ready_button.status = STARTED
            ready_button.setAutoDraw(True)
        
        # if ready_button is active this frame...
        if ready_button.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mainTrial_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mainTrial_instruct" ---
    for thisComponent in mainTrial_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('mainTrial_instruct.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # store data for thisExp (ExperimentHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    thisExp.addData('mouse.x', x)
    thisExp.addData('mouse.y', y)
    thisExp.addData('mouse.leftButton', buttons[0])
    thisExp.addData('mouse.midButton', buttons[1])
    thisExp.addData('mouse.rightButton', buttons[2])
    thisExp.nextEntry()
    # the Routine "mainTrial_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ExptLoop = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('RTtimeConditions_own.xlsx'),
        seed=None, name='ExptLoop')
    thisExp.addLoop(ExptLoop)  # add the loop to the experiment
    thisExptLoop = ExptLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExptLoop.rgb)
    if thisExptLoop != None:
        for paramName in thisExptLoop:
            globals()[paramName] = thisExptLoop[paramName]
    
    for thisExptLoop in ExptLoop:
        currentLoop = ExptLoop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisExptLoop.rgb)
        if thisExptLoop != None:
            for paramName in thisExptLoop:
                globals()[paramName] = thisExptLoop[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        # Run 'Begin Routine' code from setStimuli
        positionList = [-0.375,-0.125,0.125,0.375] #list of possible X coordinates for target to appear
        shuffle(positionList) #randomise these positions
        targetX = positionList[0] #pick the first value from the list 
        
        #thisImage is the variable in the Image field of targetImage
        if thisImage == 'images/target_square.jpg': #path of where to find the target image
            corrAns = 'v' #setting the key press that will be the correct answer
            corrButton = square_button #setting the button that will be the correct answer
            corrButtonName = 'square_button' #making this a string so that it can be compared later when checking for acccuracy
        elif thisImage == 'images/target_cross.jpg':
            corrAns = 'c'
            corrButton = cross_button
            corrButtonName = 'cross_button'
        elif thisImage == 'images/target_plus.jpg':
            corrAns = 'b'
            corrButton = plus_button
            corrButtonName = 'plus_button'
        
        
        targetImage.setPos([targetX, 0])
        targetImage.setImage(thisImage)
        keyResp.keys = []
        keyResp.rt = []
        _keyResp_allKeys = []
        # setup some python lists for storing info about the mouseResp
        mouseResp.x = []
        mouseResp.y = []
        mouseResp.leftButton = []
        mouseResp.midButton = []
        mouseResp.rightButton = []
        mouseResp.time = []
        mouseResp.clicked_name = []
        gotValidClick = False  # until a click is received
        mouseResp.mouseClock.reset()
        # keep track of which components have finished
        trialComponents = [rightright_tile, right_tile, left_tile, leftleft_tile, square_button, plus_button, cross_button, targetImage, keyResp, mouseResp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rightright_tile* updates
            
            # if rightright_tile is starting this frame...
            if rightright_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                rightright_tile.frameNStart = frameN  # exact frame index
                rightright_tile.tStart = t  # local t and not account for scr refresh
                rightright_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightright_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                rightright_tile.status = STARTED
                rightright_tile.setAutoDraw(True)
            
            # if rightright_tile is active this frame...
            if rightright_tile.status == STARTED:
                # update params
                pass
            
            # *right_tile* updates
            
            # if right_tile is starting this frame...
            if right_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                right_tile.frameNStart = frameN  # exact frame index
                right_tile.tStart = t  # local t and not account for scr refresh
                right_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                right_tile.status = STARTED
                right_tile.setAutoDraw(True)
            
            # if right_tile is active this frame...
            if right_tile.status == STARTED:
                # update params
                pass
            
            # *left_tile* updates
            
            # if left_tile is starting this frame...
            if left_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                left_tile.frameNStart = frameN  # exact frame index
                left_tile.tStart = t  # local t and not account for scr refresh
                left_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                left_tile.status = STARTED
                left_tile.setAutoDraw(True)
            
            # if left_tile is active this frame...
            if left_tile.status == STARTED:
                # update params
                pass
            
            # *leftleft_tile* updates
            
            # if leftleft_tile is starting this frame...
            if leftleft_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                leftleft_tile.frameNStart = frameN  # exact frame index
                leftleft_tile.tStart = t  # local t and not account for scr refresh
                leftleft_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftleft_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                leftleft_tile.status = STARTED
                leftleft_tile.setAutoDraw(True)
            
            # if leftleft_tile is active this frame...
            if leftleft_tile.status == STARTED:
                # update params
                pass
            
            # *square_button* updates
            
            # if square_button is starting this frame...
            if square_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                square_button.frameNStart = frameN  # exact frame index
                square_button.tStart = t  # local t and not account for scr refresh
                square_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                square_button.status = STARTED
                square_button.setAutoDraw(True)
            
            # if square_button is active this frame...
            if square_button.status == STARTED:
                # update params
                pass
            
            # *plus_button* updates
            
            # if plus_button is starting this frame...
            if plus_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                plus_button.frameNStart = frameN  # exact frame index
                plus_button.tStart = t  # local t and not account for scr refresh
                plus_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(plus_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                plus_button.status = STARTED
                plus_button.setAutoDraw(True)
            
            # if plus_button is active this frame...
            if plus_button.status == STARTED:
                # update params
                pass
            
            # *cross_button* updates
            
            # if cross_button is starting this frame...
            if cross_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                cross_button.frameNStart = frameN  # exact frame index
                cross_button.tStart = t  # local t and not account for scr refresh
                cross_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                cross_button.status = STARTED
                cross_button.setAutoDraw(True)
            
            # if cross_button is active this frame...
            if cross_button.status == STARTED:
                # update params
                pass
            
            # *targetImage* updates
            
            # if targetImage is starting this frame...
            if targetImage.status == NOT_STARTED and tThisFlip >= onsetTime-frameTolerance:
                # keep track of start time/frame for later
                targetImage.frameNStart = frameN  # exact frame index
                targetImage.tStart = t  # local t and not account for scr refresh
                targetImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(targetImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'targetImage.started')
                # update status
                targetImage.status = STARTED
                targetImage.setAutoDraw(True)
            
            # if targetImage is active this frame...
            if targetImage.status == STARTED:
                # update params
                pass
            
            # if targetImage is stopping this frame...
            if targetImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > targetImage.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    targetImage.tStop = t  # not accounting for scr refresh
                    targetImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targetImage.stopped')
                    # update status
                    targetImage.status = FINISHED
                    targetImage.setAutoDraw(False)
            
            # *keyResp* updates
            
            # if keyResp is starting this frame...
            if keyResp.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                keyResp.frameNStart = frameN  # exact frame index
                keyResp.tStart = t  # local t and not account for scr refresh
                keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                keyResp.status = STARTED
                # keyboard checking is just starting
                keyResp.clock.reset()  # now t=0
                keyResp.clearEvents(eventType='keyboard')
            if keyResp.status == STARTED:
                theseKeys = keyResp.getKeys(keyList=['b','c','v'], ignoreKeys=["escape"], waitRelease=False)
                _keyResp_allKeys.extend(theseKeys)
                if len(_keyResp_allKeys):
                    keyResp.keys = _keyResp_allKeys[-1].name  # just the last key pressed
                    keyResp.rt = _keyResp_allKeys[-1].rt
                    keyResp.duration = _keyResp_allKeys[-1].duration
                    # was this correct?
                    if (keyResp.keys == str(corrAns)) or (keyResp.keys == corrAns):
                        keyResp.corr = 1
                    else:
                        keyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *mouseResp* updates
            
            # if mouseResp is starting this frame...
            if mouseResp.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouseResp.frameNStart = frameN  # exact frame index
                mouseResp.tStart = t  # local t and not account for scr refresh
                mouseResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouseResp.status = STARTED
                prevButtonState = mouseResp.getPressed()  # if button is down already this ISN'T a new click
            if mouseResp.status == STARTED:  # only update if started and not finished!
                buttons = mouseResp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([square_button, plus_button, cross_button], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseResp):
                                gotValidClick = True
                                mouseResp.clicked_name.append(obj.name)
                        x, y = mouseResp.getPos()
                        mouseResp.x.append(x)
                        mouseResp.y.append(y)
                        buttons = mouseResp.getPressed()
                        mouseResp.leftButton.append(buttons[0])
                        mouseResp.midButton.append(buttons[1])
                        mouseResp.rightButton.append(buttons[2])
                        mouseResp.time.append(mouseResp.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # check responses
        if keyResp.keys in ['', [], None]:  # No response was made
            keyResp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               keyResp.corr = 1;  # correct non-response
            else:
               keyResp.corr = 0;  # failed to respond (incorrectly)
        # store data for ExptLoop (TrialHandler)
        ExptLoop.addData('keyResp.keys',keyResp.keys)
        ExptLoop.addData('keyResp.corr', keyResp.corr)
        if keyResp.keys != None:  # we had a response
            ExptLoop.addData('keyResp.rt', keyResp.rt)
            ExptLoop.addData('keyResp.duration', keyResp.duration)
        # store data for ExptLoop (TrialHandler)
        ExptLoop.addData('mouseResp.x', mouseResp.x)
        ExptLoop.addData('mouseResp.y', mouseResp.y)
        ExptLoop.addData('mouseResp.leftButton', mouseResp.leftButton)
        ExptLoop.addData('mouseResp.midButton', mouseResp.midButton)
        ExptLoop.addData('mouseResp.rightButton', mouseResp.rightButton)
        ExptLoop.addData('mouseResp.time', mouseResp.time)
        ExptLoop.addData('mouseResp.clicked_name', mouseResp.clicked_name)
        # Run 'End Routine' code from recordRTandAccuracy
        #this code is to record the reaction times and accuracy of the trial
        
        thisRoutineDuration = t # how long did this trial last
        
        # keyResp.rt is the time with which a key was pressed
        # mouseResp.time is the time with which a button was clicked/pressed
        # thisRecRT - how long it took for participants to respond after onset of targetImage
        # thisRespType - keeping track of which response component was used
        # thisAcc - whether or not the response was correct
        # correctMouseResp - name of column in data output which records the accuracy of mouse responses
        
        if keyResp.keys:
            thisRespType = 'keyboard' #record type of response 
            thisRecRT = keyResp.rt - onsetTime #record time taken to response
            if keyResp.corr == 1: #if the response is correct
                thisAcc = 'correct' #print correct
            else:
                thisAcc = 'incorrect'
        else:
            thisRespType = 'mouse'
            thisRecRT = mouseResp.time[0] - onsetTime
            if mouseResp.clicked_name[0] == corrButtonName: #check if what was clicked corresponds to the correct button
                thisAcc = 'correct'
                thisExp.addData('correctMouseResp', 1) #record accuracy of mouse clicks
            else:
                thisAcc = 'incorrect'
                thisExp.addData('correctMouseResp', 0)
        
        thisExp.addData('trialRespTimes', thisRecRT) #record the actual response times of each trial
        
        
        #print(thisRoutineDuration, thisRecRT, thisRespType, thisAcc, onsetTime)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 2.0 repeats of 'ExptLoop'
    
    
    # --- Prepare to start Routine "end_message" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end_message.started', globalClock.getTime())
    # keep track of which components have finished
    end_messageComponents = [end_text]
    for thisComponent in end_messageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_message" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_text* updates
        
        # if end_text is starting this frame...
        if end_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            end_text.status = STARTED
            end_text.setAutoDraw(True)
        
        # if end_text is active this frame...
        if end_text.status == STARTED:
            # update params
            pass
        
        # if end_text is stopping this frame...
        if end_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_text.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                end_text.tStop = t  # not accounting for scr refresh
                end_text.frameNStop = frameN  # exact frame index
                # update status
                end_text.status = FINISHED
                end_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_messageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_message" ---
    for thisComponent in end_messageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end_message.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)

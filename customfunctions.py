def dyetocolormap(channels):
    '''
    From the list of channels included in the image metadata, return a list of corresponding colormap names readable by napari.
    '''

    # dictionary of stain:colormap pairs
    dict = {'EGFP':'green', 'DAPI':'blue', 'mRF12':'red'}

    return [dict[x] for x in channels]

def splitchannels(array):
    '''
    From a multidimensional array, split channel axis and plot pictures for each channel.
    '''

    # split channels
    c1 = array[0, :, :]
    c2 = array[1, :, :]
    c3 = array[2, :, :]

    # plot all 3 channels
    f, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(20, 10))

    ax0.imshow(c1, cmap='Greens')
    ax0.set_title('GFP', fontsize=18)

    ax1.imshow(c2, cmap='Blues')
    ax1.set_title('DAPI', fontsize=18)

    ax2.imshow(c3, cmap='Reds')
    ax2.set_title('RFP', fontsize=18)

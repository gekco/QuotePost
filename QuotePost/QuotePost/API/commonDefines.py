
#commonDefines - contains variables that are common to all files


IS_SUCCESSFULL = 0     #every apiservice function returns a list IS_SUCCESSFULL is the first index
 					   #index of response list which contains 0 or 1 
					   # if the operation was successfull it sends 1 otherwise 0
RETURN_STRING = 1	   # 2nd index is the return string error/message. that is sent to	

IS_QUOTE = 2           #3rd Index - only present in fetch service. tells whether the string is a quote or message

#errors and responses
RESPONSE_QUOTE_POST_SAVE_SUCCESS  = "Quote Saved And Posted Successfully."
RESPONSE_FB_SUCCESS_POST_FAIL     = "Posted to Facebook ,Unable to Save Quote. "
RESPONSE_FB_POST_FAIL             = "Unable to Post the Quote to Facebook."
RESPONSE_QUOTE_ALREADY_POSTED     = "Quote Already Posted"
RESPONSE_EMPTY_QUOTE              = "Error! Empty Quote."
RESPONSE_ALREADY_SAVED_QUOTE      = "You have Already Saved This Quote"
RESPONSE_SUCCESS_SAVE             = "Successfully Saved"
RESPONSE_ALL_QUOTES_FETCHED       = "All Favourite Quotes Fetched Already."
RES_FB_AUTH_ERR                   = "Cannot Post the Quote because The Apps are not allowed to past on behalf of user unless allowed by the user"
RES_TRIES_EXCEEDED                = "We have exceeded the number of tries to save photos."
RES_SUCCESS_POST                  = "Quote Posted Successfully"
RES_INAVLID_FILE				  = "Unable to Post.Image file is invalid."
RESPONSE_SAVE_QUOTE_FAIL          = "Unable to Save Quote"
RES_QUOTE_UPDATED_IN_DB           = "Quote Updated in DB"
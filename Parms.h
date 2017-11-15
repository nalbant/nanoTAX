
#ifndef PARMS_H
#define PARMS_H

#define NUM_BASES               4                 // A, G, C, T
#define DEFAULT_OLIGMER_SIZE    11
#define SEPARATOR               ":"
#define HEADER_WORD_LENGTH      "%WORD_LENGTH"
#define ZERO_ENTRY_VALUE        -20
#define DB_MAX_UPDATES          2
#define UPDATE_THRESHOLD        250000
#define MAX_STRING_LENGTH       128

#define BASE_VALUE_A            0
#define BASE_VALUE_G            1
#define BASE_VALUE_C            2
#define BASE_VALUE_T            3


typedef enum PARMS_RunModeType 
{  
    MODE_BIN,
    MODE_BIN_WITH_REFINEMENT,
    MODE_CREATE_DATABASE,
    MODE_ADD_TO_DATABASE,
    MODE_MAX_RUN_MODE,
}; 


void            PARMS_Initialize(void); 
BOOLEAN         PARMS_ProcessCommandLine(INT argc, BYTE **argv); 
vector<string> *PARMS_GetInputFileNames(void);
string          PARMS_GetOutputFileName(void);
string          PARMS_GetDatabaseFileName(void);
INT             PARMS_GetClassificationThreshold(void); 
INT             PARMS_GetRunMode(void); 
void            PARMS_Printf(BYTE *String);
void            PARMS_Error(BYTE *String);
string          PARMS_Trim( const string& s );
void            PARMS_GetStringParts(string originalString, 
                             vector<string> *stringParts, 
                             string delimiter); 

#endif

/********************************* END OF FILE ***********************************/

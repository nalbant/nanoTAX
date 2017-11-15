
#ifndef RAIPHYDATABASE_H
#define RAIPHYDATABASE_H


#include "Globals.h"
#include "Parms.h"
#include "RAIProfiler.h"


class RAIphyDatabase 
{
    public:
        RAIphyDatabase(); 
        ~RAIphyDatabase(); 

        vector<Sequence> RAIProfiles;

        // Public Functions 
        BOOLEAN IsValid(void); 
        ULONG WordLength(void); 
        INT GetIndex(string modelName); 
        void ReadDatabase(string fileName); 
        BOOLEAN SaveDatabase(void); 
        void AddItems(vector<string> *inFileNames); 
        void CreateDatabase(vector<string> *inFilenames, string outFilename, INT wordLength);
        BOOLEAN UpdateDatabase(string outputFilename);
        void UpdateVector(INT vectorIndex, DOUBLE *tempVector);
        BOOLEAN UpdateVector(INT vectorIndex, DOUBLE *tempVector, INT vectorLength, string outputFilename); 
    
    private:
        string m_fileName; 
        BOOLEAN m_isValid;
        ULONG m_updateCount; 
        ULONG m_wordLength; 
        
        RAIProfiler m_profiler;
    
}; 

#endif

/********************************* END OF FILE ***********************************/

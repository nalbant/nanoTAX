

#ifndef RAIPROFILER_H
#define RAIPROFILER_H

#include "Globals.h"
#include "Parms.h"
#include <map>

class RAIProfiler
{
public:
    RAIProfiler();
    string ProfileFastaFile(string filename, INT wordLength, vector<Sequence> *list, BOOLEAN normalize);
    void    PrepareVector(DOUBLE* vector, INT vectorSize, INT wordLength);
    BOOLEAN ProfileNextSequence(fstream *inStream, Sequence *tempSequence, INT wordLength, SequenceCounts *tempCounts);

    map<BYTE, INT> m_hash;
};

#endif

/********************************* END OF FILE ***********************************/

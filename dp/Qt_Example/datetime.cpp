#include "datetime.h"

TDateTime::TDateTime() : QDateTime()
{
    setTime(QTime::currentTime());
    setDate(QDate::currentDate());
};

TDateTime::TDateTime(uint s) : QDateTime()
{
    setTime_t(s);
};

TDateTime::TDateTime(QDate d) : QDateTime()
{
    setDate(d);
    setTime(QTime::currentTime());
};

TDateTime::TDateTime(QTime t) : QDateTime()
{
    setTime(t);
    setDate(QDate::currentDate());
};

TDateTime::TDateTime(QString s) : QDateTime()
{
    setDate(QDateTime::fromString(s,"dd.MM.yyyy hh:mm:ss").date());
    setTime(QDateTime::fromString(s,"dd.MM.yyyy hh:mm:ss").time());
};

TDateTime TDateTime::operator+ (uint s)
{
    uint t = toTime_t() + s;
    return TDateTime(t);
};

TDateTime TDateTime::operator+= (uint s)
{
    uint t = toTime_t() + s;
    setTime_t(t);
    return *this;
};

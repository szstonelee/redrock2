#ifndef __ROCK_EVICT_H
#define __ROCK_EVICT_H

#include "server.h"

dict* init_rock_evict_dict();
void init_rock_evict_before_enter_event_loop();

void on_db_add_key_for_rock_evict(const int dbid, const sds key);
void on_db_del_key_for_rock_evict(const int dbid, const sds key);
void on_db_overwrite_key_for_rock_evict(const int dbid, const sds key);
void on_db_visit_key_for_rock_evict(const int dbid, const sds key);
void on_rockval_key_for_rock_evict(const int dbid, const sds key);
void on_recover_key_for_rock_evict(const int dbid, const sds key);
void on_empty_db_for_rock_evict(const int dbnum);


#endif
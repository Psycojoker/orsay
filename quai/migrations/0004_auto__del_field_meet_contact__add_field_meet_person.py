# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.add_column('quai_meet', 'person',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['quai.Person']),
                      keep_default=False)
        db.delete_column('quai_meet', 'contact_id')

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration. 'Meet.contact' and its values cannot be restored.")


    models = {
        'quai.mail': {
            'Meta': {'object_name': 'Mail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quai.Person']"})
        },
        'quai.meet': {
            'Meta': {'object_name': 'Meet'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quai.Person']"}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'quai.person': {
            'Meta': {'object_name': 'Person'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_recontacting_loop': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_called': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['quai']

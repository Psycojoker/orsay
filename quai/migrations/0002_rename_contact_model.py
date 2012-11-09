# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('quai_contact', 'quai_person')
        db.alter_column('quai_meet', 'contact_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quai.Person']))

    def backwards(self, orm):
        db.rename_table('quai_person', 'quai_contact')
        db.alter_column('quai_meet', 'contact_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quai.Contact']))

    models = {
        'quai.meet': {
            'Meta': {'object_name': 'Meet'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quai.Person']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
